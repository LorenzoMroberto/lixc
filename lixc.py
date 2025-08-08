# lixeira.py
import sys
import pythoncom
import win32com.client as w
import win32com.shell.shellcon as c
import win32com.shell.shell as shell
import ctypes
import os

# ✅ Chama a API do Windows diretamente
def esvaziar_lixeira():
    flags = c.SHERB_NOCONFIRMATION | c.SHERB_NOPROGRESSUI | c.SHERB_NOSOUND
    res = ctypes.windll.shell32.SHEmptyRecycleBinW(0, None, flags)
    return res == 0  # True se sucesso

def main():
    pythoncom.CoInitialize()
    args = sys.argv[1:]
    if not args:
        print("Uso: l, e, e <núm>, ou <arquivo>")
        sys.exit(1)

    cmd = args[0].lower()

    # === Comandos da lixeira: l e e ===
    if cmd in ("l", "e"):
        sh = w.Dispatch("Shell.Application")
        rb = sh.NameSpace(c.CSIDL_BITBUCKET)
        itens = list(rb.Items())

        # Listar itens
        if cmd == "l":
            for i, item in enumerate(itens, 1):
                t = "Pasta" if item.IsFolder else "Arquivo"
                print(f"{i:>2}- [{t}] ({item.Name})")

        # Esvaziar ou excluir item
        elif cmd == "e":
            if len(args) == 1:
                # ✅ Usa a API do Windows diretamente
                if esvaziar_lixeira():
                    print("Lixeira esvaziada.")
                else:
                    print("Falha ao esvaziar a lixeira.")
            else:
                try:
                    n = int(args[1])
                    item = {i+1: it for i, it in enumerate(itens)}.get(n)
                    if item:
                        # Exclui permanentemente
                        shell.SHFileOperation((
                            0, c.FO_DELETE, item.Path, None,
                            c.FOF_NOCONFIRMATION | c.FOF_SILENT | c.FOF_NOERRORUI,
                            None, None
                        ))
                    print(f"Item {n} {'excluído permanentemente.' if item else 'não encontrado.'}")
                except:
                    print("Número inválido.")

    # === Mover para lixeira ===
    else:
        p = args[0]
        if not os.path.exists(p):
            print(f"[Erro] Não encontrado: {p}")
            sys.exit(1)
        t, n = "Pasta" if os.path.isdir(p) else "Arquivo", os.path.basename(p)
        try:
            shell.SHFileOperation((
                0, c.FO_DELETE, p, None, c.FOF_ALLOWUNDO | c.FOF_NOCONFIRMATION, None, None
            ))
            print(f"[{t}] ({n}) => movido para lixeira")
        except Exception as e:
            print(f"[{t}] ({n}) => falha: {e}")

if __name__ == "__main__":
    main()
