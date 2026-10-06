"""Executa os mesmos testes nas duas versoes e captura os logs em PNG via Edge."""
import hashlib
import html
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "evidencias"
EDGE = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")


def main():
    OUT.mkdir(exist_ok=True)
    registros = []
    for numero, implementacao, esperado in [(1, "original", 1), (2, "corrigida", 0)]:
        comando = [sys.executable, "-m", "pytest", "-p", "no:cacheprovider", "-v", "--tb=short", "--color=no", "--implementacao", implementacao]
        resultado = subprocess.run(comando, cwd=ROOT, capture_output=True, text=True)
        log = resultado.stdout + resultado.stderr
        print(log)
        (OUT / f"PRINT{numero}.txt").write_text(log, encoding="utf-8")
        if resultado.returncode != esperado:
            raise RuntimeError(f"Execucao {implementacao}: codigo inesperado {resultado.returncode}")
        linhas = []
        for linha in log.splitlines():
            cor = "#ff8888" if "FAILED" in linha or linha.startswith("E ") else "#8ce99a" if "PASSED" in linha or "passed" in linha else "#e9ecef"
            linhas.append(f'<span style="color:{cor}">{html.escape(linha)}</span>')
        pagina = OUT / f"PRINT{numero}.html"
        pagina.write_text('<!doctype html><meta charset="utf-8"><style>body{background:#202124;color:#e9ecef;padding:24px}h1{font:24px sans-serif}pre{font:14px/20px Consolas,monospace;white-space:pre-wrap;overflow-wrap:anywhere}</style>' + f'<h1>PRINT{numero} — Pytest / {implementacao}</h1><pre>' + '\n'.join(linhas) + '</pre>', encoding="utf-8")
        altura = max(1100, len(log.splitlines()) * 23 + 180)
        imagem = OUT / f"PRINT{numero}.png"
        perfil = tempfile.mkdtemp(prefix="desconto-edge-")
        captura = subprocess.run([str(EDGE), "--headless", "--disable-gpu", "--no-first-run", "--no-default-browser-check", f"--user-data-dir={perfil}", f"--screenshot={imagem}", f"--window-size=1500,{altura}", pagina.as_uri()], capture_output=True, timeout=60)
        if captura.returncode:
            raise RuntimeError(f"Falha na captura: {captura.stderr.decode(errors='replace')}")
        if not imagem.is_file():
            raise RuntimeError("O navegador nao gerou o print")
        registros.append({"implementacao": implementacao, "comando": comando, "exit_code": resultado.returncode, "log_sha256": hashlib.sha256(log.encode()).hexdigest()})
    (OUT / "execucoes.json").write_text(json.dumps({"data_utc": datetime.now(timezone.utc).isoformat(), "execucoes": registros}, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
