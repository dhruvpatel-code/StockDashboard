from layout import get_layout
from server import app, cache

# Set the layout of the app
app.layout = get_layout()

# Import the callbacks module
import callbacks 

# Run the app in debug mode
if __name__ == '__main__':
    app.run_server(debug=True)







