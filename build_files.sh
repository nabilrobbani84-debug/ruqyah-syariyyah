# Install dependencies
echo "Installing requirements..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear