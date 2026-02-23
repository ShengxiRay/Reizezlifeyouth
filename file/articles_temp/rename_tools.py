import os
import re

# 这是你网站中最终保留的 45 篇文章标题（严格按照 1-45 的顺序）
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
    "感恩节说感恩",
    "遇见好心人",
    "奇妙的乐高城",
    "爸爸与Kemy的聊天记录",
    "波士顿科学博物馆游览记",
    "美国衣食住行篇",
    "11月5日爸爸写给Kemy的信",
    "11月2日爸爸写给Kemy的信",
    "快乐分享百分百",
    "奇妙的美国万圣节",
    "万圣节特辑——来自世界各地的31种可怕怪物",
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
    "多让小孩接触外面世界的意义",
    "写给Kemy的一封信",
    "美国上学篇",
    "阅读的力量，推荐两本有关关于失败的书",
    "美国到达篇",
    "分享知道的国外保健品（男士篇）",
    "美国出发篇",
    "当世界已然是地球村，你需要聆听和了解全世界，一起来了解美国波士顿(Boston)"
]

def clean_text(text):
    # 移除所有的标点符号、空格和特殊字符，只保留纯文字，提高匹配成功率
    return re.sub(r'[^\w\u4e00-\u9fff]', '', text)

def batch_rename():
    print("🚀 开始自动匹配并重命名 HTML 文件...\n")
    
    # 获取当前目录下所有的 .html 文件（排除脚本如果被误存为html）
    current_dir = os.getcwd()
    files = [f for f in os.listdir(current_dir) if f.endswith('.html') and not f[0].isdigit()]
    
    success_count = 0
    not_found_list = []

    for index, title in enumerate(article_titles):
        new_name = f"{index + 1}.html"
        
        # 提取标题的纯文本前 8 个字符作为核心匹配词（应对微信文章标题后缀的各种杂乱信息）
        clean_title = clean_text(title)
        match_keyword = clean_title[:8] if len(clean_title) >= 8 else clean_title
        
        found = False
        
        for filename in files:
            clean_filename = clean_text(filename)
            
            # 如果文件名中包含了我们的核心关键词
            if match_keyword in clean_filename:
                try:
                    os.rename(filename, new_name)
                    print(f"✅ 成功: [原名: {filename[:20]}...] -> [新名: {new_name}]")
                    files.remove(filename) # 匹配成功后从待匹配列表中移除
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
        print("\n💡 建议：请检查是否漏下载了这些文章，或者手动将漏掉的文章重命名。")

if __name__ == "__main__":
    batch_rename()