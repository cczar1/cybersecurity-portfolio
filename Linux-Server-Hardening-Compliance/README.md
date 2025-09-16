# Linux Server Hardening & Remediation

---

## Project Overview

Performed a **gap analysis and hardening exercise** on a Linux VM to identify and remediate high-risk misconfigurations. I assessed the system against security benchmarks, mapped findings to **NIST CSF 2.0**, and applied remediations to strengthen authentication, package management, bootloader security, access controls, and USB device restrictions.

This project gave me direct practice in:

- Performing system security assessments (Lynis)
- Mapping findings to security frameworks (NIST CSF 2.0)
- Hardening Linux authentication and access controls
- Applying secure configuration changes
- Documenting remediation steps and verifying effectiveness

The workflow models how security professionals perform system hardening and remediation in enterprise environments.

---

## Steps Performed

1. Conducted a baseline security assessment of a Linux server (VM) using **Lynis**
2. Identified misconfigurations (e.g., weak password policies, vulnerable packages, GRUB bootloader with no password)
3. Mapped high-risk findings to **NIST CSF 2.0** controls
4. Applied remediations
5. Verified that remediations were effective through testing and review
6. Documented results in a structured report with risks, controls, and remediation steps

---

## Artifacts

**REPORT NAVIGATION LINKS**

**Section I. Report Introductory Findings**

- [Report Introductory Findings](Report-Introductory-Findings/Report-Introductory-Findings.pdf)

**Section II. Remediation of High-Risk Items**

- [Missing Password Strength Module](Missing-password-strength-module/Missing-password-strength-module.pdf)
- [Vulnerable Packages](Vulnerable-packages/Vulnerable-packages.pdf)
- [GRUB Boot - No Password Protection](GRUB-Boot-No-password-protection/GRUB-Boot-No-password-protection.pdf)
- [Insecure File Permissions](Insecure-file-permissions/Insecure-file-permissions.pdf)
- [USB Storage Driver Not Disabled](USB-storage-driver-not-disabled/USB-storage-driver-not-disabled.pdf)

**Section III. Assessment Summary and Recommendations**

- [Assessment Summary and Recommendations](Assessment-Summary-and-Recommendations/Assessment-Summary-and-Recommendations.pdf)

**Full Report PDF:**

- <a href="Linux-Server-Security-Assessment-and-Remediation-Report.pdf" target="_blank">Linux Server Security Assessment and Remediation (PDF)</a>

Note: If viewing full report PDF in Github, please allow a few moments for PDF file to load. Github will only load a few pages at a time. Select "More Pages" (Desktop) or click "Next" (mobile) at the bottom of the screen when you reach the last loaded page.

---

## Key Takeaways

- Strengthened Linux hardening and remediation skills
- Practiced mapping technical issues to **NIST CSF 2.0** controls
- Reinforced secure configuration practices (authentication, privilege management, bootloader security, device controls)
- Produced professional-style documentation reflecting a real audit/remediation process

---

## License

This project is licensed under the MIT License.
