
```markdown
# Depend En Moi (Depend on Me) - Your ML and LLMOps Configuration Friend 👀


## 🚀 Quick Start to MLOps Automation

Depend En Moi streamlines your machine learning and LLM lifecycle management operation tools. It works by automating dependency management and environment setup. So you can focus on building and deploying your ML models faster and more efficiently. 🛠️

### Current Status
5th November 2023: **Early Development** 👼

Link: [https://github.com/nullzero-live/depend-en-moi](https://github.com/nullzero-live/depend-en-moi) 👾


### What It Does 🧐
Right now - not that much, it's brand new and the Nullzero's first module. Scary! 

Depend En Moi is a tool tailored for machine learning projects, with a special focus on MLOps & LLMOps tools such as Langchain, OpenAI (openai), Weights and Biases (wandb), MLFlow (mflow), Humanloop (humanloop.com) -- Always adding more. 

Here's what it can do for you:

- 🔍 Automatically searches and installs dependencies for your selected libraries, or defaults if no custom list is provided.
- 🔐 Safely stores your API keys in a local `.env` file for easy access and security.
- 🚫 Ensures `.env` is added to your `.gitignore` to keep secrets out of version control.
- 🐳 Adds `.env` to your `.dockerfile` if one exists in your project.
- ✅ Handles login and other necessary preliminary steps to get you up and running.

Depend-en-moi is designed to get your application ready for a quick, streamlined login, and config in LangChain, WandB, HumanLoop, MLFlow, and more...

### Always Evolving 👷

This tool is constantly being improved to support the latest in MLOps best practices and libraries. Stay tuned for updates!

### Dependencies 📦

Here are the dependencies that Depend En Moi works with out of the box:

```plaintext
cachetools==5.3.2
GitPython==3.1.0
packaging==23.2
python-dotenv==1.0.0
pipdeptree==2.13.0
tree==0.2.4
langchain==0.0.330
openai==0.28.1
wandb==0.15.12

and more... browse requirements.txt and the source codefor more information.
```

### Getting Started 🌟

To get started with Depend En Moi, simply clone this repository and run the main installation script:

```bash
git clone https://github.com/nullzero-live/depend-en-moi
cd depend-en-moi
python setup.py install
```

### Flags 🛠️
```bash
- `-n, --name`: Sets the `AUTO_INSTALL` variable to True.
- `-c, --custom`: Adds a custom library.
- `--auto`: Sets the `AUTO_INSTALL` variable to True.
- `--debug`: Sets the `DEBUG` variable to True.
- `--logging`: Sets the `LOGGING` variable to True.
- `-q, --quiet`: Suppresses the output.
- `-l, --level`: Sets the logging level. (Note: The action may need to be changed to `store` instead of `store_true` if a value is to be provided)
- `-t, --type`: Specifies the Type of App (LLM, ML, Web). (Note: The action may need to be changed to `store` instead of `store_true` if a value is to be provided)
- `-v, --version`: Displays the version of DependMLOps.

```

### Contributing 🤝

Interested in contributing? We love pull requests and issues from fellow MLOps enthusiasts. Fork away and submit your PR as necessary.

This is a very underdeveloped library that I will continue to work on. I'd be interested in seeing how others are able to improve it for optimizing MLOps and LLMOps

### License ⚖️

Depend En Moi is open-source software [licensed as MIT](LICENSE).

---

Made with 💖 and a lot of ☕ by [Nullzero](<https://github.com/nullzero-live/>).
```

---


## Aha-To-Do List

### ToDo:
- [ ] **Get rid of the github stuff from the library
- [ ] **Complete argparser for intuitive use**
- [ ] **Add a "--c" flag to arg_parser to add custom libraries**
- [ ] **Abstract out the library types for incorporation of any library**
- [ ] **Include MLFlow and Humanloop config**
- [ ] **Parse out the syntax from each**
- [ ] **Option to dump dependencies or next steps into an external file**

### Done ✅
- [x] **.Devcontainer**
- [x] **_constants**
- [x] **utils**
- [x] **main**
- [x] **planned structure**
- [x] ** Library c'est complete

### And dennnnn......
- [ ] ❌ **Very little (help a fellow out!)**

🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗

-- Nullzero


