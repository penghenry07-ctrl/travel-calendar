from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder='.')
CORS(app)

# 数据文件路径
DATA_FILE = 'trips_data.json'

def load_trips():
    """从文件加载旅行数据"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_trips(trips):
    """保存旅行数据到文件"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(trips, f, ensure_ascii=False, indent=2)

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
    trips = load_trips()
    return jsonify(trips)

@app.route('/api/trips', methods=['POST'])
def save_all_trips():
    """保存所有旅行计划"""
    try:
        trips = request.json
        save_trips(trips)
        return jsonify({"success": True, "message": "保存成功"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/api/trips/<int:index>', methods=['DELETE'])
def delete_trip(index):
    """删除指定的旅行计划"""
    try:
        trips = load_trips()
        if 0 <= index < len(trips):
            trips.pop(index)
            save_trips(trips)
            return jsonify({"success": True, "message": "删除成功"})
        return jsonify({"success": False, "message": "索引无效"}), 400
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/health')
def health():
    """健康检查接口"""
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})

if __name__ == '__main__':
    # 开发环境
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
