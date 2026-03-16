# 🌍 TerraPilot

> Python-driven Terraform automation — manage your entire infrastructure lifecycle from a single script.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple?style=flat-square&logo=terraform)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?style=flat-square&logo=amazonaws)
![DevOps](https://img.shields.io/badge/DevOps-Automation-green?style=flat-square)

</div>

---

## 🎬 See It In Action

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=00D9FF&center=true&vCenter=true&width=500&lines=Terraform+Init...+✅;Planning+Infrastructure...+✅;Applying+Changes...+✅;Infrastructure+Ready!+🚀" alt="Typing animation" />
</div>

---

## 🚀 What is TerraPilot?

Stop typing `terraform init`, `terraform plan`, `terraform apply` manually.

TerraPilot wraps your entire Terraform workflow in a single Python script — automating initialization, planning, applying, and destroying infrastructure with zero manual CLI intervention. Built for DevOps engineers who value speed, consistency, and repeatability.

---

## ⚙️ How It Works
```
┌──────────────┐      ┌─────────────────┐      ┌──────────────────┐
│  terra.py    │─────▶│  subprocess     │─────▶│  Terraform CLI   │
│  (Python)    │      │  (automation)   │      │  init/apply/destroy│
└──────────────┘      └─────────────────┘      └──────────────────┘
                                                        │
                                                        ▼
                                               ┌──────────────────┐
                                               │   AWS Resources  │
                                               │  EC2 · SG · Keys │
                                               └──────────────────┘
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **Full Automation** | Runs `init`, `plan`, `apply`, `destroy` via Python |
| ⚡ **Zero Manual CLI** | No terminal commands needed after setup |
| 🔁 **Consistent Execution** | Same result every run — no human error |
| ☁️ **AWS Ready** | Provisions EC2, Security Groups, Key Pairs |
| 🧹 **Clean Teardown** | Automated destroy prevents cost overruns |

---

## ⚡ Quick Start
```bash
# 1. Clone
git clone https://github.com/Erharshita-cloud/TerraPilot.git
cd TerraPilot

# 2. Verify Terraform
terraform -version

# 3. Configure AWS credentials
aws configure

# 4. Launch
python terra.py
```

---

## 📸 Output

| EC2 Instance | Security Group | Key Pair |
|---|---|---|
| ![instance](images/instance.png) | ![sg](images/securitygroup.png) | ![key](images/key.png) |

---

## 📂 Project Structure
```
TerraPilot/
├── terraform/        # HCL configuration files
├── terra.py          # Python automation engine
├── images/           # Output screenshots
└── README.md
```

---

## 🤝 Contributing
PRs and suggestions welcome!

**Harshita Goel** · DevOps & Cloud Engineer
[GitHub](https://github.com/Erharshita-cloud) · harshitagoel1503@gmail.com

---

<div align="center">⭐ Star this repo if it helped you!</div>
