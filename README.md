# 🌟 Reiz EZ Life Youth Home

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

> **A Place to Grow, Belong, & Become. | 一个可以成长、归属，并成为自己的地方。**

Welcome to the official repository for the **Reiz EZ Life Youth Home** web platform. This project serves as the digital front door for our nonprofit organization, dedicated to helping newly arrived Chinese students and children of immigrants transition smoothly into life in the U.S.

## 📖 About The Project (项目简介)

Arriving in a new country can be an isolating experience—facing language barriers, cultural differences, and an unfamiliar school system. **Reiz EZ Life** was founded to turn that uncertainty into confidence. 

This website provides a supportive digital space featuring:
- **Life & Growth (生活与成长):** Resources to help students adapt quietly and confidently.
- **Safety & Resources (关系与安全感):** A curated collection of the founder's personal stories and tips.
- **Agency & Application (主体性与升学):** Guidance for academic success.

## ✨ Key Features (核心亮点)

- 🍎 **Apple-Style Glassmorphism UI**: A modern, clean, and immersive aesthetic using advanced CSS3 backdrop-filters and radial gradients.
- 🌐 **Seamless Bilingual Support (EN/中)**: Built-in Vanilla JavaScript state management allows users to switch between English and Chinese instantly without reloading the page.
- 📱 **Fully Responsive Design**: Fluid CSS Grid layout that adapts beautifully to desktops, tablets, and mobile devices.
- 📚 **Integrated Article Reader System**: A custom-built modal system that loads and displays a curated list of historical WeChat Official Account articles directly within the site.
- 💌 **Interactive Modals**: Custom, animated pop-ups for the Founder's Welcome message and "Join Us" contact actions.

## 🛠 Tech Stack (技术栈)

This project is built with pure, lightweight web technologies to ensure maximum performance and zero dependency overhead:
- **HTML5** (Semantic structure)
- **CSS3** (CSS Grid, Flexbox, CSS Variables, Animations)
- **Vanilla JavaScript (ES6)** (DOM manipulation, Event delegation, State management)
- **Python 3** (Utility scripts for automated content management)

## 📁 Project Structure (文件结构)

```text
reiz-ez-life-youth-home/
│
├── index.html              # Main entry point (UI & Logic)
├── rename_tools.py         # Python utility script for batch renaming articles
├── README.md               # Project documentation
│
└── articles/               # Directory for locally hosted article files
    ├── 1.html              # Exported article 1
    ├── 2.html              # Exported article 2
    └── ...                 # Articles up to 45.html
```

## 🚀 Getting Started (本地运行指南)

Since this is a static website, getting it up and running is incredibly simple.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/reiz-ez-life-youth-home.git](https://github.com/yourusername/reiz-ez-life-youth-home.git)
   ```
2. **Open the project:**
   Navigate to the project folder and simply open `index.html` in your favorite web browser (Chrome, Safari, Edge).
   *Alternatively, use the VS Code "Live Server" extension for hot-reloading during development.*

## 📝 Content Management: Updating Articles (文章管理)

To bypass WeChat's strict anti-hotlinking (X-Frame-Options) policies and ensure a seamless in-app reading experience, articles are hosted locally. We provide a Python automation script to streamline this workflow.

**How to add or update articles:**
1. Export the desired WeChat articles as `.html` files (e.g., using the SingleFile browser extension).
2. Place the downloaded `.html` files into a temporary folder alongside `rename_tools.py`.
3. Run the automation script:
   ```bash
   python3 rename_tools.py
   ```
4. The script will automatically match the filenames with our database, rename them to `1.html`, `2.html`, etc.
5. Move the renamed files into the `/articles/` directory of the project.

## 🤝 Contributing (参与贡献)

We welcome contributions! Whether you want to improve the UI, translate content, or add new features, your help is appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📫 Contact (联系我们)

**Kemy (Huang Yuannan)** - Founder & President  
Email: [contact@reizezlife.org](mailto:contact@reizezlife.org)  
Phone: +1 (617) 659-5400  
Website: [www.reizezlife.org](https://www.reizezlife.org)

---
*Building a strong, supported start in a new home. 💛*