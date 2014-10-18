from socket import *

def main():   
      
    HOST = "1.234.91.200"
    PORT = 110        
    
    s = socket(AF_INET, SOCK_STREAM)           
    s.connect((HOST,PORT))     
    data = s.recv(1024) 
    
    print (data)           
    s.close()

if __name__ == '__main__':
    main()