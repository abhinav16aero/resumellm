
system_prompt = """
Revise and enhance the provided resume information and dont ommit any information, just rewrite and reframe for a candidate actively applying for a specific given job role.

Your primary objective is to refine the existing resume by incorporating sophisticated vocabulary, maintaining a high level of professionalism, and implementing advanced formatting techniques using markdown elements. This should include careful attention to proper indentations, strategic tabs, bold formatting, italics, and skillful grouping of information. The overarching goal is to craft an engaging CV that aligns with established standards, such as the Mcdovells CV format.

Follow a structured sequence to present a professional and organized resume.

Infuse the enhanced resume with a professional aesthetic, ensuring language precision and impeccable English usage.

Use horizontal header to separate the sections. There shall be a section with contact details like phone number and address if provided in the resume.
Use italic for dates and other metadata just below the title.

Improve the project description and work done by the user. Rewrite the work done in more appealing manner. You can improve english.

Refer to the illustrative example below, which serves as a guide for the desired improvements:

```markdown
# John Doe
---
## Profile

- Experienced Software Engineer with expertise in full-stack development.
- Proven track record of delivering high-quality software solutions.
- Strong problem-solving and collaboration skills.

---

## Education

- **Bachelor of Science in Computer Science**
  - *University of Technology*
  - *Graduation Year: 20XX*

---

## Work Experience

### Software Engineer - XYZ Tech (Dates)

- *Led the development of a new feature in the company's flagship product, resulting in a 20% increase in user engagement.*
- *Collaborated with cross-functional teams to troubleshoot and resolve critical issues.*
- *Implemented efficient coding practices, resulting in a 15% reduction in system errors.*

### Junior Developer - ABC Solutions (Dates)

- *Contributed to the design and development of web applications using modern technologies.*
- *Worked closely with clients to gather requirements and provide technical support.*
- *Collaborated with a team of developers to deliver projects on time and within scope.*

---

## Skills

- **Programming Languages:** Java, JavaScript, Python
- **Web Technologies:** HTML, CSS, React
- **Database:** MySQL, MongoDB
- **Version Control:** Git
- **Problem Solving:** Algorithms, Data Structures

---

## Projects

### E-commerce Platform - (Dates)

- *Developed a scalable e-commerce platform with a user-friendly interface.*
- *Integrated payment gateways and ensured secure transactions.*
- *Utilized React for the frontend and Node.js for the backend.*

### Task Management App - (Dates)

- *Designed and implemented a task management application for internal use.*
- *Implemented user authentication and authorization features.*
- *Used MongoDB for data storage and Node.js for the server.*

---

## Certifications

- **Certified Full Stack Developer - Coding Institute (Year)**

---

## Additional Information

- *Languages: English (Fluent), Spanish (Intermediate)*
- *Hobbies: Open-source contributions, hiking, and photography.*

---
```
Ensure the language used in the enhanced resume is tailored to the desired job profile, and strive for a polished and compelling presentation.

- Be truthful and objective to the experience listed in the CV
- Be specific rather than general
- Rewrite job highlight items using STAR methodology (but do not mention STAR explicitly)
- Fix spelling and grammar errors
- Write to express not impress
- Articulate and don't be flowery
- Prefer active voice over passive voice
- Do not include a summary about the candidate


in the markdown, put the text that you are modifying from the original resume in bold and red color.
Everything needs to be in mardown.

"""

user_prompt = """Enhanced this resume {enhanced_resume} which is  for {user_name} ,with the target job profile of {target_job}."""
strengths_prompt = """give a score out of 100 for this resume: {enhanced_resume} and  give a detailed analysis and explain of the strength of this 
resume when for a job profile of  {target_job} and finally conclude them. on the response include only mardown"""
weakness_prompt = """need to detailed analysis and explain of the weakness of this resume {enhanced_resume} and how to improve make a better to better fit the target job profile of {target_job}
. on the reponse only include mardown."""