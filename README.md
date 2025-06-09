# Professional Photo Maker

A web application that enhances photos to create professional-looking images using OpenCV and modern web technologies.

## Features

- Image upload and processing
- Professional photo enhancement
- Real-time preview
- Multiple enhancement options
- Download processed images

## Tech Stack

### Backend
- FastAPI
- OpenCV
- Python 3.8+
- Additional Python libraries for image processing

### Frontend
- React
- Material-UI
- Modern JavaScript (ES6+)

## Project Structure

```
ProfessionalPhotoMaker/
├── backend/           # FastAPI backend
│   ├── app/
│   ├── requirements.txt
│   └── README.md
├── frontend/          # React frontend
│   ├── src/
│   ├── package.json
│   └── README.md
└── README.md
```

## Setup Instructions

### Backend Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup
1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Run the development server:
   ```bash
   npm start
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 