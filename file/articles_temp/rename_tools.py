import os
import re

# 这是你网站中最终保留的 39 篇文章标题（严格按照 1-39 的顺序）
article_titles = [
    "Kemy与Jason的阅读小课堂-How Spider save the sun",
    "英语成语：(Happy Part) ~~~",
    "英你而语—for your English",
    "难忘的美国夏令营",
    "Fright dream day",
    "我和最强大脑王峰&李威的近距离接触",
    "迪士尼邮轮上过春节",
    "奥兰多之行",
    "上医院",
    "小提琴表演记",
    "补发Pierce School滑冰记滑雪视频",
    "第一次亲密接触击剑",
    "Pierce School滑冰记",
    "写在圣诞节前",
    "波士顿的第二场雪",
    "波士顿的第一场雪",
    "遇见好心人",
    "奇妙的乐高城",
    "爸爸与Kemy的聊天记录",
    "波士顿科学博物馆游览记",
    "11月5日爸爸写给Kemy的信",
    "11月2日爸爸写给Kemy的信",
    "快乐分享百分百",
    "奇妙的美国万圣节",
    "10月31日爸爸写给Kemy的信",
    "美国生活趣事",
    "10月20日Kemy写给爸爸的信",
    "爸爸回国了",
    "父亲的回信",
    "哈佛大学和MIT",
    "Kemy写给老师同学们的一封信",
    "波士顿美术博物馆之行",
    "美国学记",
    "美国游览篇",
    "写给Kemy的一封信",
    "美国上学篇",
    "美国到达篇",
    "美国出发篇",
    "当世界已然是地球村，你需要聆听和了解全世界，一起来了解美国波士顿(Boston)"
]

def clean_text(text):
    return re.sub(r'[^\w\u4e00-\u9fff]', '', text)

def batch_rename():
    print("🚀 开始自动匹配并重命名 HTML 文件...\n")
    
    current_dir = os.getcwd()
    files = [f for f in os.listdir(current_dir) if f.endswith('.html') and not f[0].isdigit()]
    
    success_count = 0
    not_found_list = []

    for index, title in enumerate(article_titles):
        new_name = f"{index + 1}.html"
        
        clean_title = clean_text(title)
        match_keyword = clean_title[:8] if len(clean_title) >= 8 else clean_title
        
        found = False
        
        for filename in files:
            clean_filename = clean_text(filename)
            
            if match_keyword in clean_filename:
                try:
                    os.rename(filename, new_name)
                    print(f"✅ 成功: [原名: {filename[:20]}...] -> [新名: {new_name}]")
                    files.remove(filename) 
                    success_count += 1
                    found = True
                    break
                except Exception as e:
                    print(f"❌ 错误: 无法重命名 {filename}. 原因: {e}")
        
        if not found:
            not_found_list.append(f"ID {index + 1}: {title}")

    print("\n" + "="*40)
    print(f"🎉 任务结束！共成功更名 {success_count} 个文件。")
    
    if not_found_list:
        print(f"\n⚠️ 以下 {len(not_found_list)} 篇文章未找到对应的 HTML 文件：")
        for item in not_found_list:
            print(f"  - {item}")

if __name__ == "__main__":
    batch_rename()