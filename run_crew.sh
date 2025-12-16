#!/bin/bash
# 通用 CrewAI 示例运行脚本
# 用法: ./run_crew.sh <crew_name> [args...]
# 示例: ./run_crew.sh markdown_validator README.md

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

echo "运行: $CREW_NAME"
echo "路径: $MAIN_PY"
echo "参数: $ARGS"
echo "---"

PYTHONPATH="$SRC_DIR" /opt/homebrew/anaconda3/bin/conda run -n crew-ai python "$MAIN_PY" $ARGS
