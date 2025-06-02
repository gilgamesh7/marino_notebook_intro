# marino_notebook_intro
An introduction ti the Reactive marimo notebook, a replacement for Jupyter

# Links
- [Marimo: A Reactive, Reproducible Notebook](https://realpython.com/marimo-notebook/#why-linear-notebooks-dont-quite-cut-it-anymore)
- [Marimo](https://marimo.io)
- [Marimo API Reference](https://docs.marimo.io/api/)

# Setup environment locally
- Create virtual environment : uv init .
- Install marimo : uv add marimo  
- Install other packages for this project :
    - uv add numpy
    - uv add matplotlib

# Use locally
- start notebook : marimo edit simultaneous_equations.py (opens in browser)
- Sandboxing 
    - marimo edit --sandbox notebook.py: Allows you to create a new notebook or edit an existing one in a sandbox. It also checks the required dependencies and offers to install them if they’re absent. What’s more, marimo continues to maintain package tracking as you update the notebook.    
    - marimo run --sandbox notebook.py: Allows you to open an existing notebook in a sandbox, install the required dependencies, and run the notebook in read-only mode.
    - marimo new --sandbox: Allows you to create a new notebook in a sandboxed environment.