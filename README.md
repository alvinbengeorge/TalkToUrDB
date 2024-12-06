# Sample <PYTHON/FASTAPI>

This project aims to simplify the use of DBMS, by integrating a chatbot to SQL. You ask it what to do, it will do for you. NO MORE SQL QUERIES! JUST QUERIES! IN ENGLISH!

---

## 🚀 Getting Started  

### Open Using Daytona  

1. **Install Daytona**: Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/).  
2. **Create the Workspace**:  
   ```bash  
   daytona create <SAMPLE_REPO_URL> 
   ```  

... MORE STEPS IF NEEDED ...

4. **Start the Application**:  
   ```bash
   pip3 install -r requirements.txt;
   echo "GEMINI_API_KEY=<your api key>";
   fastapi run &;
   cd client/;
   pnpm i;
   pnpm build;
   pnpm start &;
   ```  

---

## ✨ Features  

- realtime chat app
- seamless connection with db
- multiple sessions to multiple connections
- simple frontend ui
