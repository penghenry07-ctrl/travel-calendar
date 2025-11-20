from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder='.')
CORS(app)

# Supabase配置 - 使用正确的URL和Key
SUPABASE_URL = 'https://ddiddpxhwtksvevcnaqf.supabase.co'
SUPABASE_KEY = 'sb_publishable_BsBOFfR-ommhctDc71A7QA_gtLS20bt'

def get_supabase_data():
    """从Supabase获取数据"""
    try:
        response = requests.get(
            f'{SUPABASE_URL}/rest/v1/trips_data?select=data&order=id.desc&limit=1',
            headers={
                'apikey': SUPABASE_KEY,
                'Authorization': f'Bearer {SUPABASE_KEY}'
            },
            timeout=10
        )
        
        print(f'GET Response Status: {response.status_code}')
        
        if response.ok and response.json():
            return response.json()[0]['data']
        return []
    except Exception as e:
        print(f'Error loading from Supabase: {e}')
        return []

def save_supabase_data(trips_data):
    """保存数据到Supabase"""
    try:
        # 先检查是否存在记录
        check_response = requests.get(
            f'{SUPABASE_URL}/rest/v1/trips_data?select=id&limit=1',
            headers={
                'apikey': SUPABASE_KEY,
                'Authorization': f'Bearer {SUPABASE_KEY}'
            },
            timeout=10
        )
        
        print(f'Check existing records: {check_response.status_code}')
        
        if check_response.ok and check_response.json():
            # 有记录，使用PATCH更新
            record_id = check_response.json()[0]['id']
            response = requests.patch(
                f'{SUPABASE_URL}/rest/v1/trips_data?id=eq.{record_id}',
                json={'data': trips_data, 'updated_at': datetime.now().isoformat()},
                headers={
                    'apikey': SUPABASE_KEY,
                    'Authorization': f'Bearer {SUPABASE_KEY}',
                    'Content-Type': 'application/json',
                    'Prefer': 'return=minimal'
                },
                timeout=10
            )
            print(f'PATCH Response: {response.status_code}')
        else:
            # 没有记录，使用POST插入
            response = requests.post(
                f'{SUPABASE_URL}/rest/v1/trips_data',
                json={'data': trips_data, 'updated_at': datetime.now().isoformat()},
                headers={
                    'apikey': SUPABASE_KEY,
                    'Authorization': f'Bearer {SUPABASE_KEY}',
                    'Content-Type': 'application/json',
                    'Prefer': 'return=minimal'
                },
                timeout=10
            )
            print(f'POST Response: {response.status_code}')
        
        if response.ok or response.status_code == 201:
            print('Save successful!')
            return True
        else:
            print(f'Save failed: {response.status_code} - {response.text}')
            return False
            
    except Exception as e:
        print(f'Error saving to Supabase: {e}')
        import traceback
        traceback.print_exc()
        return False

@app.route('/')
def index():
    """提供前端页面"""
    return send_from_directory('.', 'index.html')

@app.route('/apple-touch-icon.png')
def apple_icon():
    """提供 Apple Touch Icon"""
    return send_from_directory('.', 'apple-touch-icon.png')

@app.route('/favicon.ico')
def favicon():
    """提供 favicon"""
    return send_from_directory('.', 'favicon.ico')

@app.route('/api/trips', methods=['GET'])
def get_trips():
    """获取所有旅行计划"""
    trips = get_supabase_data()
    return jsonify(trips)

@app.route('/api/trips', methods=['POST'])
def save_all_trips():
    """保存所有旅行计划"""
    try:
        trips = request.json
        print(f'Saving {len(trips)} trips')
        success = save_supabase_data(trips)
        
        if success:
            return jsonify({"success": True, "message": "保存成功"})
        else:
            return jsonify({"success": False, "message": "保存失败"}), 500
    except Exception as e:
        print(f'Save endpoint error: {e}')
        import traceback
        traceback.print_exc()
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/api/trips/<int:index>', methods=['DELETE'])
def delete_trip(index):
    """删除指定的旅行计划"""
    try:
        trips = get_supabase_data()
        if 0 <= index < len(trips):
            trips.pop(index)
            success = save_supabase_data(trips)
            
            if success:
                return jsonify({"success": True, "message": "删除成功"})
            else:
                return jsonify({"success": False, "message": "删除失败"}), 500
        return jsonify({"success": False, "message": "索引无效"}), 400
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/health')
def health():
    """健康检查接口"""
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
