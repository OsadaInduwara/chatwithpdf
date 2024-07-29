from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "<title>Chat with PDF</title>" in response.text


def test_upload_pdf():
    with open("sample.pdf", "rb") as pdf_file:
        response = client.post("/upload/", files={"file": pdf_file})
        assert response.status_code == 200
        assert "text" in response.json()


def test_chat_with_pdf():
    sample_text = "This is a sample text extracted from a PDF."
    sample_question = "What is this text about?"

    response = client.post(
        "/chat/",
        json={"text": sample_text, "question": sample_question}
    )
    assert response.status_code == 200
    assert "answer" in response.json()
