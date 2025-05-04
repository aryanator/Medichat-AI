# Set variables
$keyPath = "C:\Users\aryan\Downloads\hc-chatbot-key.pem"
$ec2Address = "ec2-user@3.88.227.40"
$destinationPath = "/home/ubuntu/chatbot"

# Create the destination directory on the EC2 instance
ssh -i $keyPath $ec2Address "mkdir -p $destinationPath"

# Transfer files and folders
scp -i $keyPath -r "C:\CHATBOT\intent_classifier_minimal" ${ec2Address}:${destinationPath}
scp -i $keyPath -r "C:\CHATBOT\generator_minimal" ${ec2Address}:${destinationPath}
scp -i $keyPath "C:\CHATBOT\label_encoder.pkl" ${ec2Address}:${destinationPath}
