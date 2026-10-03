from ingest import load_documents_from_dir


def test_load_documents_from_dir_reads_text_files(tmp_path):
    file_one = tmp_path / "one.txt"
    file_one.write_text("hello world", encoding="utf-8")

    file_two = tmp_path / "two.md"
    file_two.write_text("# Example\nThis is a markdown file.", encoding="utf-8")

    documents = load_documents_from_dir(str(tmp_path))

    assert len(documents) == 2
    contents = [doc["page_content"] for doc in documents]
    assert any("hello world" in content for content in contents)
    assert any("Example" in content for content in contents)
    assert any(doc["metadata"]["source"] == "two.md" for doc in documents)
