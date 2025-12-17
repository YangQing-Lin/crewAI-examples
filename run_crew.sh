#!/bin/bash
# 通用 CrewAI 示例运行脚本
# 用法: ./run_crew.sh <crew_name> [args...]
# 示例: ./run_crew.sh markdown_validator README.md
#
# 环境优先级: .venv > uv > conda > 系统 python

set -e

# 加载 .env 文件
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

CREW_NAME=$1
shift
ARGS="$@"

if [ -z "$CREW_NAME" ]; then
    echo "用法: ./run_crew.sh <crew_name> [args...]"
    echo "可用示例:"
    ls -1 crews/
    exit 1
fi

# 查找 crew 目录和 main.py
CREW_DIR="crews/$CREW_NAME"
if [ ! -d "$CREW_DIR" ]; then
    echo "错误: 未找到 $CREW_DIR"
    exit 1
fi

# 查找 src 目录下的 main.py
MAIN_PY=$(find "$CREW_DIR/src" -name "main.py" 2>/dev/null | head -1)
SRC_DIR=$(dirname $(dirname "$MAIN_PY"))

if [ -z "$MAIN_PY" ]; then
    echo "错误: 未找到 main.py"
    exit 1
fi

# 确定 Python 执行方式
get_python_cmd() {
    # 1. 优先使用项目根目录的 .venv
    if [ -f ".venv/bin/python" ]; then
        echo ".venv/bin/python"
        return
    fi

    # 2. 检查 crew 目录的 .venv
    if [ -f "$CREW_DIR/.venv/bin/python" ]; then
        echo "$CREW_DIR/.venv/bin/python"
        return
    fi

    # 3. 使用 uv run（如果有 uv 且有 pyproject.toml）
    if command -v uv &>/dev/null; then
        if [ -f "pyproject.toml" ] || [ -f "$CREW_DIR/pyproject.toml" ]; then
            echo "uv run python"
            return
        fi
    fi

    # 4. 尝试 conda（macOS）
    if [ -f "/opt/homebrew/anaconda3/bin/conda" ]; then
        echo "/opt/homebrew/anaconda3/bin/conda run -n crew-ai python"
        return
    fi

    # 5. 尝试 conda（Linux 常见路径）
    if [ -f "$HOME/anaconda3/bin/conda" ]; then
        echo "$HOME/anaconda3/bin/conda run -n crew-ai python"
        return
    fi

    # 6. 回退到系统 python3
    echo "python3"
}

PYTHON_CMD=$(get_python_cmd)

echo "运行: $CREW_NAME"
echo "路径: $MAIN_PY"
echo "Python: $PYTHON_CMD"
[ -n "$ARGS" ] && echo "参数: $ARGS"
echo "---"

PYTHONPATH="$SRC_DIR" $PYTHON_CMD "$MAIN_PY" $ARGS
