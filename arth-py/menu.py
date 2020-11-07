def aws_setup():
    try:
        os.system("aws --version")
    except:
        os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip'")
        os.system("unzip awscliv2.zip")
        os.system("sudo ./aws/install")
    return

def aws_key_create():
    os.system("tput setaf 50")
    os.system("aws configure")
    key_name=input("Enter key name:")
    os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
    return


def instance_launch():
    os.system("tput setaf 50")
    os.system("aws configure")
    img_id=input("Enter image id of ec2 instance:")
    sub_id=input("Enter subnet id:")
    key=input("Enter key name:")
    cnt=input("Enter count of instances:")
    inst_type=input("Enter instance type:")
    os.system("tput setaf 10")
    os.system("aws ec2 run-instances --image-id {} --count {} --instance-type {} --key-name {} --subnet-id {} --associate-public-ip-address".format(img_id,cnt,inst_type,key,sub_id))
    return

def webserver():
    os.system("tput setaf 50")
    ip=input("Enter IP of instance to be configured:")
    key=input("Enter key name:")
    os.system("tput setaf 10")
    os.system("ssh -i {}.pem ec2-user@{} sudo yum install httpd".format(key,ip))
    os.system("scp -i {}.pem web.html ec2-user@{}:/home/ec2-user".format(key,ip))
    os.system("ssh -i {}.pem ec2-user@{} sudo cp /web.html /var/www/html".format(key,ip))
    os.system("ssh -i {}.pem ec2-user@{} sudo systemctl start httpd".format(key,ip))
    return

import os

os.system("tput setaf 11")
print("-*"*40)

os.system("tput setaf 14")
print("-"*35,"Welcome!","-"*35)

os.system("tput setaf 11")
print("-*"*40)

os.system("tput setaf 12")
#print("#"*36)
print("\n\n")

cont=1

while True:
    print("""\tPress 1:To run linux commands\n\tPress 2:To run aws commands\n\tPress 3:To run hadoop commands\n\tPress 4:To run docker commands\n\tPress 5:To exit\n""")
    os.system("tput setaf 50")
    ch_core=input("Enter your choice:")
    try:
        ch_core=int(ch_core)
    except:
        os.system("tput setaf 9")

    if ch_core==1:
        break

    elif ch_core==2:
        while True:
            os.system("tput setaf 12")
            print("""\n\tPress 1:To create key pair\n\tPress 2:To launch EC2 instance\n\tPress 3:To configure EC2 instance as web server\n\tPress 4:To stop instance\n\tPress 5:To terminate EC2 instance\n\tPress 6:To start stopped instance\n\tPress 7:To create S3 bucket\n\tPress 8:Upload object\n\tPress 9.Make object public\n\tPress 10:Delete object\n\tPress 11:Delete bucket\n\tPress 12:To create EBS volume\n\tPress 13:To attach EBS volume\n\tPree 14:To detach volume\n\tPress 15:To create cloudfront distribution\n\tPress 16:To create user\n\tPress 17:To exit\n""")
            os.system("tput setaf 50")
            aws_inp=input("Enter your choice:")

            try:
                aws_inp=int(aws_inp)
            except:
                os.system("tput setaf 9")
            print("\n\n")
            os.system("tput setaf 10")

            if aws_inp==1:
                os.system("clear")
                aws_setup()
                aws_key_create()

            elif aws_inp==2:
                os.system("clear")
                aws_setup()
                instance_launch()

            elif aws_inp==3:
                os.system("clear")
                aws_setup()
                webserver()

            elif aws_inp==4:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                os.system("aws configure")
                inst_id=input("Enter id of instance to be stopped:")
                os.system("tput setaf 10")
                os.system("aws ec2 stop-instances --instance-ids {}".format(inst_id))

            elif aws_inp==5:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                #os.system("aws configure")
                t_id=input("Enter id of instance to be terminated:")
                os.system("tput setaf 10")
                os.system("aws ec2 terminate-instances --instance-ids {}".format(t_id))

            elif aws_inp==6:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                os.system("aws configure")
                st_id=input("Enter id of instance to be started:")
                os.system("tput setaf 10")
                os.system("aws ec2 start-instances --instance-ids {}".format(st_id))

            elif aws_inp==7:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                os.system("aws configure")
                buck_name=input("Enter bucket name(should be unique):")
                region=input("Enter region:")
                os.system("tput setaf 10")
                os.system("aws s3 mb s3://{} --region {}".format(buck_name,region))

            elif aws_inp==8:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                #os.system("aws configure")
                buck_name=input("Enter bucket name:")
                obj=input("Enter object:")
                os.system("tput setaf 10")
                os.system("aws s3 cp {} s3://{}/{}".format(obj,buck_name,obj))

            elif aws_inp==9:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                #os.system("aws configure")
                bucket_name=input("Enter bucket name:")
                obj_name=input("Enter object name:")
                os.system("tput setaf 10")
                os.system("aws s3api put-object-acl --bucket {} --key {} --acl public-read".format(buck_name,obj_name))

            elif aws_inp==10:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                #os.system("aws configure")
                buck_name=input("Enter bucket name:")
                obj=input("Enter object:")
                os.system("tput setaf 10")
                os.system("aws s3 rm s3://{}/{}".format(buck_name,obj))

            elif aws_inp==11:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                #os.system("aws configure")
                del_buck_name=input("Enter bucket name:")
                os.system("tput setaf 10")
                os.system("aws s3 rb s3://{}".format(del_buck_name))
        
            elif aws_inp==12:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                #os.system("aws configure")
                size=input("Enter volume size:")
                v_type=input("Enter volume type:")
                az=input("Enter availability zone:")
                os.system("tput setaf 10")
                os.system("aws ec2 create-volume --availability-zone {} --volume-type {} --size {}".format(az,v_type,size))


            elif aws_inp==13:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                #os.system("aws configure")
                v_id=input("Enter volume id:")
                inst_id=input("Enter instance id:")
                device=input("Enter device:")
                os.system("tput setaf 10")
                os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(v_id,inst_id,device))

            elif aws_inp==14:
                os.system("tput setaf 50")
                vol=input("Enter id of volume to be detached:")
                os.system("tput setaf 10")
                os.system("aws ec2 detach-volume --volume-id {}".format(vol))
            elif aws_inp==15:
                os.system("clear")
                os.system("tput setaf 50")
                aws_setup()
                #os.system("aws configure")
                o_domain=input("Enter origin domain:")
                os.system("tput setaf 10")
                os.system("aws cloudfront create-distribution --origin-domain-name {}".format(o_domain))

            elif aws_inp==16:
                os.system("clear")
                os.system("tput setaf 50")
                user_name=input("Enter user name:")
                os.system("tput setaf 10")
                os.system("aws iam create-user --user-name {}".format(user_name))

            elif aws_inp==17:
                os.system("clear")
                os.system("tput setaf 7")
                break

            else:
                os.system("tput setaf 9")
                print("Please Enter valid option")


    elif ch_core==5:
        os.system("tput setaf 7")
        os.system("clear")
        exit()

os.system("tput setaf 7")




    
