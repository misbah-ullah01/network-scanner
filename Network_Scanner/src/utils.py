def is_valid(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0<= int(part) <= 255:
            return False
    return True

def format_output(results):
    formatted_results = []
    for ip, status in results.items():
        formatted_results.append(f"{ip}: {'Active' if status else 'Inactive'}")
    return "\n".join(formatted_results)

def handle_exception(e):
    print(f"An error occured: {e}")