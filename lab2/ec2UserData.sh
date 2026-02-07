#!/bin/bash
set -euo pipefail

yum update -y
yum install -y httpd

systemctl start httpd
systemctl enable httpd

mkdir -p /var/www/html

TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" -s)

curl -H "X-aws-ec2-metadata-token: $TOKEN" -s \
  http://169.254.169.254/latest/meta-data/local-ipv4 > /tmp/local_ipv4 &
curl -H "X-aws-ec2-metadata-token: $TOKEN" -s \
  http://169.254.169.254/latest/meta-data/placement/availability-zone > /tmp/az &
curl -H "X-aws-ec2-metadata-token: $TOKEN" -s \
  http://169.254.169.254/latest/meta-data/network/interfaces/macs/ > /tmp/macid &
wait

macid=$(head -n 1 /tmp/macid | tr -d '\n')
local_ipv4=$(cat /tmp/local_ipv4)
az=$(cat /tmp/az)

vpc=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s \
  "http://169.254.169.254/latest/meta-data/network/interfaces/macs/${macid}vpc-id")

cat > /var/www/html/index.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>EC2 Lab 2 - Instance Details</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #0f172a;
      color: #e5e7eb;
      text-align: center;
      padding: 40px;
    }
    h1, h2, h3 {
      margin-bottom: 10px;
    }
    .container {
      max-width: 900px;
      margin: 0 auto;
      background-color: #020617;
      border-radius: 12px;
      padding: 30px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
    }
    section {
      margin-top: 25px;
      margin-bottom: 25px;
      border-bottom: 1px solid #1f2937;
      padding-bottom: 20px;
    }
    section:last-of-type {
      border-bottom: none;
    }
    img {
      max-width: 280px;
      border-radius: 8px;
      margin-top: 15px;
    }
    .meta {
      text-align: left;
      margin-top: 15px;
      display: inline-block;
    }
    footer {
      margin-top: 25px;
      font-size: 0.8rem;
      color: #9ca3af;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>AWS EC2 Lab 2</h1>
    <h2>Created by: JMK </h2>

    <section id="photos">
      <h3>Travel Photos</h3>
      <img src="https://media.istockphoto.com/id/518198022/photo/saint-basils-cathedral-on-red-square-in-moscow.jpg?s=612x612&w=0&k=20&c=CCw4aMlJtwcdQu-RxKVyg1FgYzrPlRVHC2U8TLADYwM="
           alt="Saint Basil’s Cathedral in Moscow"
           style="max-width:300px; margin:10px; border-radius:10px;">
      <img src="https://www.welgrowgroup.com/img.php?file=welgrowgroupuploadsNew/country/images/cnt_157129030374_vietnam-2.jpg"
           alt="Vietnam Landscape"
           style="max-width:300px; margin:10px; border-radius:10px;">
      <img src="https://cdn.shortpixel.ai/spai/q_lossless+w_1076+h_538+to_webp+ret_img/nomadicfire.com/wp-content/uploads/2023/08/Nomadic-FIRE-Colombia-Medellin-Nightlife-Cover.jpg"
           alt="Medellin"
           style="max-width:300px; margin:10px; border-radius:10px;">
    </section>

    <section id="about">
      <h3>About Me</h3>
      <p>My name is JMK. This page was generated automatically by an EC2 User Data startup script as part of Lab 2.</p>
    </section>

    <section id="project">
      <h3>Project Description</h3>
      <p>
        This EC2 instance is running Apache (httpd) on Amazon Linux 2. At launch time, the User Data script:
      </p>
      <ul style="text-align:left; display:inline-block;">
        <li>Installed and started the Apache web server</li>
        <li>Used IMDSv2 to securely query EC2 instance metadata</li>
        <li>Generated this HTML file and placed it in <code>/var/www/html/index.html</code></li>
      </ul>
    </section>

    <section id="details">
      <h3>Instance Details & Contact</h3>
      <div class="meta">
        <p><b>Instance Name (hostname):</b> $(hostname -f)</p>
        <p><b>Private IP Address:</b> ${local_ipv4}</p>
        <p><b>Availability Zone:</b> ${az}</p>
        <p><b>VPC ID:</b> ${vpc}</p>
      </div>
      <p style="margin-top:15px;">
        If you need to reach me about this lab, please contact me through the class Facebook or class Discord.
      </p>
    </section>

    <footer>
      &copy; 2026 - EC2 Startup Script Lab (Lab 2)
    </footer>
  </div>
</body>
</html>
EOF

rm -f /tmp/local_ipv4 /tmp/az /tmp/macid
