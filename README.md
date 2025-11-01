# CVE_2025_62527_PoC

<img width="403" height="746" alt="image" src="https://github.com/user-attachments/assets/6632d1ec-3b92-46ea-9b45-1d2b6fb02ce8" />

## Overview
A **password reset link poisoning vulnerability** (CVE-2025-62527) was identified in **Taguette**, an open-source qualitative research tool.  
This issue affects **versions prior to 1.5.0** and was **publicly disclosed on October 20, 2025**.

The vulnerability allows an attacker to craft and send **malicious password reset links** to legitimate users.  
If a victim clicks the tampered link, their account credentials could be compromised or redirected to an attacker-controlled domain.

For more information, see the [GitHub Security Advisory](https://github.com/remram44/taguette/security/advisories/GHSA-7rc8-5c8q-jr6j).

---


## Setup

python3 -m venv taguette.virtualenv
. taguette.virtualenv/bin/activate
pip install taguette==1.4.3




git clone https://github.com/Mitchellzhou1/CVE_2025_62527_PoC.git
touch taguette.db

taguette --no-browser server config.py



