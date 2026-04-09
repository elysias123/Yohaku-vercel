import os

msg = message.decode("utf-8", errors="replace")
co = os.environ.get("CO_AUTHOR_VALUE", "").strip()
if not co:
    return message
line = f"Co-authored-by: {co}"
if line.lower() in msg.lower():
    return message
return (msg + "\n\n" + line + "\n").encode("utf-8")
