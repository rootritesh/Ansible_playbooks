- hosts: localhost
  vars:
    - user: USERNAME
    - pass: P4SSW0Rd
  tasks:
    - name: Sending email using gmail SMTP server
      mail:
        host: smtp.gmail.com
        port: 587
        username: "{{ user }}"
        password: "{{ pass }}"
        to: xyz@.com
        subject: "This is subject"
        body: "this is body"
