#!/usr/bin/env python3
"""
Department Manager - 部门管理脚本
用于创建、管理和委派任务给 AI 子代理部门
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

DATA_DIR = Path.home() / ".openclaw" / "department-manager"
DATA_FILE = DATA_DIR / "departments.json"

def ensure_data_dir():
    """确保数据目录存在"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text(json.dumps({"departments": [], "tasks": []}, indent=2))

def load_data():
    """加载部门数据"""
    ensure_data_dir()
    return json.loads(DATA_FILE.read_text())

def save_data(data):
    """保存部门数据"""
    DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False))

def create_department(name: str, description: str, model: str = "dashscope-coding/qwen3.5-plus"):
    """创建新部门"""
    data = load_data()
    
    # 检查是否已存在
    for dept in data["departments"]:
        if dept["name"] == name:
            print(f"❌ 部门 '{name}' 已存在")
            return False
    
    # 创建新部门
    new_dept = {
        "name": name,
        "description": description,
        "model": model,
        "created_at": datetime.now().isoformat(),
        "tasks": [],
        "status": "active"
    }
    
    data["departments"].append(new_dept)
    save_data(data)
    print(f"✅ 部门 '{name}' 创建成功")
    print(f"   描述：{description}")
    print(f"   模型：{model}")
    return True

def list_departments():
    """列出所有部门"""
    data = load_data()
    
    if not data["departments"]:
        print("📭 暂无部门")
        return
    
    print("\n🏢 已创建的部门:")
    print("=" * 60)
    
    for i, dept in enumerate(data["departments"], 1):
        status_icon = "🟢" if dept["status"] == "active" else "🔴"
        print(f"\n{i}. {status_icon} {dept['name']}")
        print(f"   描述：{dept['description']}")
        print(f"   模型：{dept['model']}")
        print(f"   任务数：{len(dept['tasks'])}")
        print(f"   创建时间：{dept['created_at']}")
    
    print("=" * 60)

def assign_task(dept_name: str, task: str, priority: str = "normal"):
    """分配任务到部门"""
    data = load_data()
    
    # 查找部门
    dept = None
    for d in data["departments"]:
        if d["name"] == dept_name:
            dept = d
            break
    
    if not dept:
        print(f"❌ 部门 '{dept_name}' 不存在")
        return False
    
    # 创建任务
    new_task = {
        "id": len(data["tasks"]) + 1,
        "dept": dept_name,
        "task": task,
        "priority": priority,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "completed_at": None,
        "output": None
    }
    
    data["tasks"].append(new_task)
    dept["tasks"].append(new_task["id"])
    save_data(data)
    
    print(f"✅ 任务已分配到 '{dept_name}' 部门")
    print(f"   任务 ID: {new_task['id']}")
    print(f"   优先级：{priority}")
    print(f"   内容：{task}")
    return True

def show_status(dept_name: str = None):
    """显示部门状态"""
    data = load_data()
    
    if dept_name:
        # 显示特定部门
        dept = next((d for d in data["departments"] if d["name"] == dept_name), None)
        if not dept:
            print(f"❌ 部门 '{dept_name}' 不存在")
            return
        
        print(f"\n📊 {dept_name} 部门状态:")
        print("=" * 60)
        print(f"描述：{dept['description']}")
        print(f"模型：{dept['model']}")
        print(f"状态：{'🟢 活跃' if dept['status'] == 'active' else '🔴 停用'}")
        
        # 显示任务
        dept_tasks = [t for t in data["tasks"] if t["id"] in dept["tasks"]]
        if dept_tasks:
            print(f"\n任务列表 ({len(dept_tasks)} 个):")
            for task in dept_tasks:
                status_icon = {"pending": "⏳", "in_progress": "🔄", "completed": "✅", "failed": "❌"}.get(task["status"], "❓")
                print(f"  {status_icon} [ID:{task['id']}] {task['task'][:50]}...")
        else:
            print("\n暂无任务")
    else:
        # 显示所有部门
        list_departments()

def show_active_tasks():
    """显示所有活跃任务"""
    data = load_data()
    
    active_tasks = [t for t in data["tasks"] if t["status"] in ["pending", "in_progress"]]
    
    if not active_tasks:
        print("✅ 无活跃任务")
        return
    
    print("\n📋 活跃任务:")
    print("=" * 60)
    
    for task in active_tasks:
        status_icon = {"pending": "⏳", "in_progress": "🔄"}.get(task["status"], "❓")
        print(f"\n{status_icon} 任务 ID: {task['id']}")
        print(f"   部门：{task['dept']}")
        print(f"   优先级：{task['priority']}")
        print(f"   内容：{task['task']}")
        print(f"   创建时间：{task['created_at']}")
    
    print("=" * 60)

def complete_task(task_id: int, output: str):
    """完成任务"""
    data = load_data()
    
    task = next((t for t in data["tasks"] if t["id"] == task_id), None)
    if not task:
        print(f"❌ 任务 {task_id} 不存在")
        return False
    
    task["status"] = "completed"
    task["completed_at"] = datetime.now().isoformat()
    task["output"] = output
    
    save_data(data)
    print(f"✅ 任务 {task_id} 已完成")
    return True

def show_report():
    """生成部门报告"""
    data = load_data()
    
    print("\n" + "=" * 60)
    print("📊 部门工作报告")
    print("=" * 60)
    print(f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    for dept in data["departments"]:
        print(f"\n🏢 {dept['name']}")
        print("-" * 40)
        
        dept_tasks = [t for t in data["tasks"] if t["id"] in dept["tasks"]]
        completed = len([t for t in dept_tasks if t["status"] == "completed"])
        pending = len([t for t in dept_tasks if t["status"] == "pending"])
        in_progress = len([t for t in dept_tasks if t["status"] == "in_progress"])
        
        print(f"   总任务：{len(dept_tasks)}")
        print(f"   ✅ 已完成：{completed}")
        print(f"   ⏳ 待处理：{pending}")
        print(f"   🔄 进行中：{in_progress}")
        
        # 显示最近完成的任务
        recent_completed = [t for t in dept_tasks if t["status"] == "completed"][-3:]
        if recent_completed:
            print(f"\n   最近完成:")
            for task in recent_completed:
                print(f"     • {task['task'][:40]}...")
    
    print("\n" + "=" * 60)

def remove_department(name: str):
    """删除部门"""
    data = load_data()
    
    dept = next((d for d in data["departments"] if d["name"] == name), None)
    if not dept:
        print(f"❌ 部门 '{name}' 不存在")
        return False
    
    data["departments"] = [d for d in data["departments"] if d["name"] != name]
    save_data(data)
    print(f"✅ 部门 '{name}' 已删除")
    return True

def print_help():
    """打印帮助信息"""
    print("""
🏢 Department Manager - 部门管理工具

用法:
  python3 departments.py <command> [options]

命令:
  create     创建新部门
             --name "部门名" --description "描述" --model "模型"
  
  list       列出所有部门
  
  assign     分配任务到部门
             --dept "部门名" --task "任务内容" --priority "优先级"
  
  status     查看部门状态
             --dept "部门名" (可选)
  
  active     查看所有活跃任务
  
  complete   完成任务
             --task-id <ID> --output "输出内容"
  
  report     生成部门报告
  
  remove     删除部门
             --name "部门名"

示例:
  python3 departments.py create --name "research" --description "信息搜索" --model "qwen3.5-plus"
  python3 departments.py assign --dept "research" --task "搜索 AI 新闻" --priority high
  python3 departments.py report
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)
    
    command = sys.argv[1]
    
    # 解析参数
    args = {}
    i = 2
    while i < len(sys.argv):
        if sys.argv[i].startswith("--"):
            key = sys.argv[i][2:]
            if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith("--"):
                args[key] = sys.argv[i + 1]
                i += 2
            else:
                args[key] = True
                i += 1
        else:
            i += 1
    
    # 执行命令
    if command == "create":
        if not args.get("name") or not args.get("description"):
            print("❌ 需要 --name 和 --description 参数")
            sys.exit(1)
        create_department(args["name"], args["description"], args.get("model", "dashscope-coding/qwen3.5-plus"))
    
    elif command == "list":
        list_departments()
    
    elif command == "assign":
        if not args.get("dept") or not args.get("task"):
            print("❌ 需要 --dept 和 --task 参数")
            sys.exit(1)
        assign_task(args["dept"], args["task"], args.get("priority", "normal"))
    
    elif command == "status":
        show_status(args.get("dept"))
    
    elif command == "active":
        show_active_tasks()
    
    elif command == "complete":
        if not args.get("task-id") or not args.get("output"):
            print("❌ 需要 --task-id 和 --output 参数")
            sys.exit(1)
        complete_task(int(args["task-id"]), args["output"])
    
    elif command == "report":
        show_report()
    
    elif command == "remove":
        if not args.get("name"):
            print("❌ 需要 --name 参数")
            sys.exit(1)
        remove_department(args["name"])
    
    elif command == "help" or command == "--help":
        print_help()
    
    else:
        print(f"❌ 未知命令：{command}")
        print_help()
        sys.exit(1)
