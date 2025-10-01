Motivated by real-world hacking incidents exploiting Korea Security
Applications (KSA) 2.0 from North Korea in 2023, we conducted a comprehensive
security investigation into its vulnerabilities. For over a decade, KSA 2.0 has
been mandated in South Korea for financial services, making it nearly
ubiquitous on PCs nationwide. While designed to enhance security through
measures such as secure communication, keylogger prevention, and antivirus
protections, KSA 2.0 can bypass sandbox mechanisms, violating modern web
security policies.

Our analysis uncovered critical flaws, including inconsistencies with web
browser threat models, improper TLS usage, sandbox violations, and inadequate
privacy safeguards. We identified 19 vulnerabilities that expose users to
serious risks, such as keylogging, man-in-the-middle attacks, private key
leakage, remote code execution, and device fingerprinting.  These
vulnerabilities were reported to government officials and vendors and have
since been patched.

To understand the security implications of KSA 2.0, we conducted two user
studies. First, our survey of 400 participants revealed widespread KSA 2.0
adoption, with 97% of banking service users having installed it, despite 59%
not understanding its functions. Second, our desktop analysis of 48 users’
systems found an average of 9 KSA installations per user, with many running
outdated versions from 2022 or earlier. These findings suggest potential
security concerns arising from the widespread deployment of KSA 2.0 in
practice.

