# serve.py
"""
Chạy LangGraph server cho graph task_maistro.
Đặt file này cùng thư mục với task_maistro.py
Rồi dùng Start Command: python serve.py
"""

from langgraph.server import serve  # import hàm serve chính thức của LangGraph

if __name__ == "__main__":
    # Tham số:
    # "task_maistro:graph" = tên file (task_maistro.py) + tên biến graph bên trong (graph)
    # host="0.0.0.0" = cho phép truy cập từ ngoài
    # port=10000 = cổng server
    serve("task_maistro:graph", host="0.0.0.0", port=10000)
