# Evolution of cybersecurity

## Common attacks & effectiveness

### Phishing

- use of digital communication to trick people into giving sensitive info or deploy malware.

- subtypes of phishing :-

    | subtype                         | description                                                                                                   |
    |---------------------------------|---------------------------------------------------------------------------------------------------------------|
    | Business Email Compromise (BEC) | Threat actors send emails from known email addresses to appear legitimate.                                    |
    | Spear Phishing                  | Malicious emails targeting specific users or groups, often appearing to be from trusted sources.              |
    | Whaling                         | A form of spear phishing that specifically targets org executives for sensitive data access.       |
    | Vishing                         | Exploitation of electronic voice communication to obtain sensitive information or impersonate a known source. |
    | Smishing                        | Use of text messages to trick users into revealing sensitive information or impersonating a known source.     |

## Social Engineering

- manuplating  technique for private info, access, or valuables via human error.
- It is highly effective technique for breaching orgs.
- Social engineering relies on false trust and lies.

- subtypes of social engineering :-

    | subtype                      | description                                                                                                                                      |
    |------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
    | Social Media Phishing        | A threat actor collects detailed information about their target from social media sites and initiates an attack using the gathered information.  |
    | Watering Hole Attack         | A threat actor targets a website frequently visited by a specific group of users and launches attacks to exploit their systems.                  |
    | USB Baiting                  | A threat actor strategically leaves a malware-infected USB stick for an employee to find and unknowingly infect their network upon installation. |
    | Physical Social Engineering  | A threat actor impersonates an employee, customer, or vendor to gain unauthorized access to a physical location or sensitive information.        |

- principles of social engineering :-

    | tactics                   | desc                                                                                                      |
    |---------------------------|-----------------------------------------------------------------------------------------------------------|
    | Authority                 | impersonate individuals with power to exploit people's conditioned respect and obedience to authority.    |
    | Intimidation              | use bullying tactics, persuading and intimidating victims into complying with their demands.              |
    | Consensus/Social proof    | leverage the trust people place in others' actions by pretending to be legitimate based on social proof.  |
    | Scarcity/Urgency          | imply that goods/services are in limited supply or an immiediate need of something                        |
    | Familiarity               | establish a fake emotional connection with users to exploit their trust and vulnerability.                |
    | Trust                     | develop an emotional relationship with users over time to gain trust and extract personal information.    |

## CISSP security domains


| Domain                               | Description                                                                                                                                              | Example                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Security & Risk Management          | &bull; Defining security goals and objectives, risk mitigation, compliance, business continuity, and adherence to relevant laws.                           | `N/A`                                                                                 |
| Asset Security                      | &bull; Securing digital and physical assets, including the storage, maintenance, retention, and proper disposal of data and equipment.                     | Tasked with securely disposing of old equipment                                       |
| Security Architecture & Engineering | &bull; Optimizing data security by implementing effective tools, systems, and processes, such as configuring firewalls and other safeguards.               | Configuring a firewall to restrict unauthorized access to the organization's network. |
| Communications & Network Security   | &bull; Managing and securing physical networks and wireless communications, including analyzing user behavior within the organization.                     | Analyzing user behavior within the org's network to detect suspicious activity.       |
| Identity & Access Management        | &bull; Keeping data secure by ensuring users follow established policies <br> - Authenticating employee identities and logging access roles.               | `N/A`                                                                                 |
| Security Assessment & Testing       | &bull; Conducting penetration testing, collecting and analyzing data, and performing security audits to identify risks, threats, and vulnerabilities.      | `N/A`                                                                                 |
| Security Operations                 | &bull; Conducting investigations, implementing preventive measures, and adhering to organizational policies and procedures to mitigate potential threats.  | `N/A`                                                                                 |
| Software Development Security       | &bull; Incorporating secure coding practices and integrating security measures into the software development lifecycle to ensure data security.            | ensuring data is properly secured and managed for an app that is built                |

## types of attacks


| Attack Type                         | Related to                                                                               | Description                                                                          | Types                                       |
|-------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|---------------------------------------------|
| Password Attacks                    | Communication and Network Security                                                       | Attempts to access password-secured devices                                          | 1. Brute Force<br>2. Rainbow Table          |
| Social Engineering                  | Security and Risk Management                                                             | Manipulates individuals to gain unauthorized access or sensitive information         | [here](#social-engineering)                 |
| Physical Attack                     | Asset Security                                                                           | Affects both digital and physical systems<br> eg: card skimming, malicious USB stick | `N/A`                                       |
| Adversarial Artificial Intelligence | Communication and Network Security, Identity and Access Management                       | Exploits AI/ML to conduct more efficient attacks                                     | `N/A`                                       |
| Supply-Chain Attack                 | Security and Risk Management, Security Architecture and Engineering, Security Operations | Targets dependencies, third-party entities, or devices that an application relies on | `N/A`                                       |
| Cryptographic Attack                | Communication and Network Security                                                       | Affects secure forms of communication between client and server                      | 1. Birthday<br>2. Collision<br>3. Downgrade |

## types of threat actors

- Advanced persistent threats (APTs)
    - highly advanced / significant expertise.
    - thorough research to remain undetected for extent period
    - intentions may include :-
        - damage critical infrastructure, such as the power grid and natural resources
        -  access to [IPs](## "intellectual property"), such as trade secrets /  patents

- Insider threats
    - types :-
        - Sabotage
        - Corruption
        - Espionage
        - Unauthorized data access or leaks

- Hacktivists
    - goals may include :-
        - Demonstrations
        - Propaganda
        - Social change campaigns
        - Fame

## types of hackers

- white hat
- semi-authorized / cybersecurity researchers
- black hat
- contracted
- vigilantes (anti black-hat)
