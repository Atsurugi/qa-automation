def test_penjumlahan():
    hasil = 2 +3 
    assert hasil == 5

def test_string():
    nama = "QA Automation"
    assert "QA" in nama

def test_list():
    buah = ["apel","mangga","jeruk"]
    assert len(buah) == 3
    assert "mangga" in buah