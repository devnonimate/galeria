import os

# Função para criar as linhas de imagem no HTML
def generate_image_tag(image_path):
    return f'<img src="{image_path}" alt="{os.path.basename(image_path)}" style="width:200px;height:auto;margin:10px;">\n'

# Função para mapear as imagens e gerar o arquivo index.html
def generate_html_gallery(base_dir, output_file='index.html'):
    folders = [f"Server-B{i}" for i in range(1, 15)]  # Pastas de Server-B1 a Server-B14
    image_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    images = []

    # Mapeia as imagens dentro de todas as pastas
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if os.path.exists(folder_path):
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in image_extensions):
                        image_path = os.path.relpath(os.path.join(root, file), base_dir)
                        images.append(image_path)

    # Gera o arquivo index.html com todas as imagens
    with open(os.path.join(base_dir, output_file), 'w', encoding='utf-8') as f:
        f.write("<html><head><title>Image Gallery</title></head><body>\n")
        f.write("<h1>Gallery of Images</h1>\n")
        f.write("<div style='display:flex;flex-wrap:wrap;'>\n")
        for image in images:
            f.write(generate_image_tag(image))
        f.write("</div>\n")
        f.write("</body></html>\n")

    print(f"Galeria de imagens criada com sucesso em {os.path.join(base_dir, output_file)}")

# Define o diretório base onde estão as pastas Server-B1 a Server-B14
base_directory = os.path.dirname(os.path.abspath(__file__))

# Gera a galeria de imagens
generate_html_gallery(base_directory)
