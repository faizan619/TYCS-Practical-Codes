package practical5;
import java.security.KeyPairGenerator;
public class Practical5 { 
    public static void main(String[] args) {
        // TODO code application logic here
        if(args.length != 1){
            System.out.println("usage : name of the file to sign ");
        }
        else try{
            KeyPairGenerator keyGen = KeyPairGenerator.getInstance("DSA","SUN");
            SecureRandom random = SecureRandom.getInstance("SHA1PRNG","SUN");   
            keyGen.initalize(1024,random);
            KeyPair pair = keyGen.generateKeyPair();
            PrivateKey priv = pair.getPrivate();
            PublicKey pub = pair.getPublic();    
            Signature dsa = Signature.getInstance("SHA1 with DSA","SUN");
            dsa.initSign(priv);
            
            FileInputStream fis = new FileInputStream("D:\\Digital Signature Demo\\digital.txt");
            BufferedInputStream bufin = new BufferedInputStream(fis);
            byte[] buffer = new byte[1024];
            int len;
            while(bufin.available() != 0){
                len = bufin.read(buffer);
                dsa.update(buffer,0,len);
            };
            bufin.close();
        }
    }
}
