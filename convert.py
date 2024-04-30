import markdown
from bs4 import BeautifulSoup
import os

def convert_md_to_html(md_file):
    
    with open(md_file, 'r',encoding='utf-8') as f:
        markdown_text = f.read()
            
    html = markdown.markdown(markdown_text,extensions=['tables'])
    return html   

def get_logo_list(md_file):
    html_content = convert_md_to_html(md_file)
    soup = BeautifulSoup(html_content, 'html.parser')

    data = {}
    for td in soup.find_all('td'):
        # print(td.get_text())
        if td.img:
            data[td.previous_sibling.previous.get_text()] = td.img['src']
            
    return data


if __name__ == '__main__':
    
    #loop files in md dir    
    md_files = []
    
    directory='md'    
    for filename in os.listdir(directory):
        if filename.endswith('.md'):  # 确保文件是以.md结尾的Markdown文件
            file_path = os.path.join(directory, filename)
            md_files.append(file_path)    
    
    logo_list={}
    for md_file in md_files:
        tmp_list = get_logo_list(md_file)
        logo_list.update(tmp_list)
    
    with open('logo_list.txt', 'w',encoding='utf-8') as f:
        for k,v in logo_list.items():
            f.write(k+','+v+'\n')
        # f.write(str(logo_list))
    # print(logo_list)   

