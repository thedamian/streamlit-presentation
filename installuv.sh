echo "Installing/updating uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh
echo "Creating/updating venv..."
uv venv
echo "Activating venv..."
 source .venv/bin/activate
echo "Installing/updating dependencies..."
uv sync
echo "All done!"
