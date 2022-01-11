import android.util.Base64;
import java.security.MessageDigest;
import java.security.spec.AlgorithmParameterSpec;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.*;

class AESUtil {
    protected String iv;
    protected String key;

    AESUtil() {
        generateKeyAndIV();
    }

    public String getIV() {
        return this.iv;
    }

    public String getKey() {
        return this.key;
    }

    public void setKey(String s1) {
        this.key = s1;
    }

    public void setIV(String s2) {
        this.iv = s2;
    }

    public void generateKeyAndIV() {
        this.iv = "0123456789abcdef";
        byte[] ivBytes = "0123456789abcdef".getBytes();
        byte[] a = new byte[16];
        a[0] = (byte) ((ivBytes[13] + ivBytes[12]) - (ivBytes[1] + ivBytes[2]));
        a[2] = (byte) ((((ivBytes[11] * 2) - (ivBytes[0] * 3)) - ivBytes[2]) + 1);
        a[15] = (byte) ((a[2] * 16) - (51 / a[2]));
        a[9] = (byte) ((((((ivBytes[3] + ivBytes[4]) + ivBytes[5]) + 1) - ivBytes[0]) - ivBytes[1]) / 3);
        a[1] = (byte) ((((a[0] * 2) - a[15]) - (ivBytes[2] * 2)) + a[9]);
        a[3] = (byte) (a[0] - 36);
        a[4] = (byte) (a[0] / a[9]);
        a[5] = (byte) (a[6] * (a[9] / 2));
        a[6] = (byte) ((a[9] / 2) - a[2]);
        a[5] = (byte) (a[6] * (a[9] / 2));
        a[7] = a[4];
        a[8] = (byte) ((((a[7] * a[6]) + ((a[2] * a[4]) * a[7])) - a[0]) - (a[0] / 10));
        a[13] = (byte) (((ivBytes[2] * 2) - (a[0] / 2)) - a[2]);
        a[10] = (byte) ((ivBytes[13] - ivBytes[2]) - a[13]);
        a[11] = (byte) ((a[9] * 4) + a[2]);
        a[12] = (byte) (a[9] + a[2]);
        a[14] = a[8];
        String s = "";
        for (int i = 0; i < 16; i++) {
            a[i] = (byte) (a[i] ^ ivBytes[i]);
            s = s + ((char) a[i]);
        }
        this.key = s;
    }

    public static byte[] encrypt(String ivStr, String keyStr, byte[] bytes) throws Exception {
        byte[] keyBytes = keyStr.getBytes("UTF-8");
        AlgorithmParameterSpec ivSpec = new IvParameterSpec(ivStr.getBytes("UTF-8"));
        SecretKeySpec newKey = new SecretKeySpec(keyBytes, "AES");
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(1, newKey, ivSpec);
        return cipher.doFinal(bytes);
    }

    public String encryptStrAndToBase64(String pt) throws Exception {
        return new String(Base64.encode(encrypt(this.iv, this.key, pt.getBytes("UTF-8")), 2), "UTF-8");
    }

    public byte[] decrypt(String ivStr, String keyStr, byte[] bytes) throws Exception {
        byte[] keyBytes = keyStr.getBytes("UTF-8");
        AlgorithmParameterSpec ivSpec = new IvParameterSpec(ivStr.getBytes("UTF-8"));
        SecretKeySpec newKey = new SecretKeySpec(keyBytes, "AES");
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(2, newKey, ivSpec);
        return cipher.doFinal(bytes);
    }

    public String decryptStrAndFromBase64(String ct) throws Exception {
        return new String(decrypt(this.iv, this.key, Base64.decode(ct.getBytes("UTF-8"), 2)), "UTF-8");
    }

    public byte[] getSHA256(String pltext) throws Exception {
        MessageDigest sha = MessageDigest.getInstance("SHA-256");
        sha.update(pltext.getBytes());
        return sha.digest();
    }

    public String bytesToHex(byte[] hash) {
        StringBuilder hexString = new StringBuilder(hash.length * 2);
        for (byte b : hash) {
            String hex = Integer.toHexString(b & 255);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }
        return hexString.toString();
    }
}


public class Solve {
    public static void main(String[] args)
    {
        AESUtil aes = new AESUtil();
        aes.generateKeyAndIV();
        System.out.println("key: "+aes.iv);
        System.out.println("iv: "+aes.key);
        try
        {
            String[] payloads = {"j2ufmtiNlIaY2r7UZp4hzFJZiotz2fKyjKluuLTg2z0=", "N//DovsAarhy+ZjLJz22oug4eOFGDvrLsvobAMTTBQ4=", "AMc5r0JQAK8y0I5EwIDrOWSqV5bGjsyatKz3vO85dwo=", "RNzeXXb7Za3QOnaC3lSNQXkwHhRX8iTNnuj6kvre2sM=", "y8Kx98A6zYTu3nr1L9lE4GpZfwt2DPB5jxAgOT9Yub4e+bHp6OLB6EQm+yEMeKZJ", "0F9pHiR7TsIRgkxwKt8wbIjWSSQYNh6zMkw+zN+l7k5xQtCHXKjZ+8J4McuBqzks", "wl3C1ZzMRUSTiPV+0R8s4n1zkOiN+mdhmHGrKsP0PWA=", "H5dOB8SGqG/3tfdOLf++uiM4ZyW3r6POqV5N2rNJsGc=", "AMc5r0JQAK8y0I5EwIDrOWSqV5bGjsyatKz3vO85dwo=", "0tDkaJflB/+a21GZAZollxAJafxsFtbFsl/KRE7p8SI=", "RfObjXK5Xwxud4/yvsnjskgh94ZPd4zZzk9bhp9sBzOH+r1ccDd05icN0wWx48sy", "9XIGNQRkYuVFUqcUOklYlg59FPmWWhwxfY4ynytLjZ4=", "9XIGNQRkYuVFUqcUOklYlmfx+NTSob58DCl9npyrfYsOOyRIegEQgWnixTPvmCDQ", "RNzeXXb7Za3QOnaC3lSNQXkwHhRX8iTNnuj6kvre2sM=", "y8Kx98A6zYTu3nr1L9lE4GpZfwt2DPB5jxAgOT9Yub4e+bHp6OLB6EQm+yEMeKZJ", "wl3C1ZzMRUSTiPV+0R8s4p75xObwQXgdsmwD8xZrB3g=", "wl3C1ZzMRUSTiPV+0R8s4sYIYWwgyISYO+Td+eBXaR8=", "AMc5r0JQAK8y0I5EwIDrOWSqV5bGjsyatKz3vO85dwo=", "N//DovsAarhy+ZjLJz22oug4eOFGDvrLsvobAMTTBQ4=", "y8Kx98A6zYTu3nr1L9lE4GpZfwt2DPB5jxAgOT9Yub4e+bHp6OLB6EQm+yEMeKZJ", "RNzeXXb7Za3QOnaC3lSNQXkwHhRX8iTNnuj6kvre2sM=", "wl3C1ZzMRUSTiPV+0R8s4n1zkOiN+mdhmHGrKsP0PWA=", "0F9pHiR7TsIRgkxwKt8wbIjWSSQYNh6zMkw+zN+l7k5xQtCHXKjZ+8J4McuBqzks", "AMc5r0JQAK8y0I5EwIDrOWSqV5bGjsyatKz3vO85dwo=", "H5dOB8SGqG/3tfdOLf++uiM4ZyW3r6POqV5N2rNJsGc=", "RfObjXK5Xwxud4/yvsnjskgh94ZPd4zZzk9bhp9sBzOH+r1ccDd05icN0wWx48sy", "0tDkaJflB/+a21GZAZollxAJafxsFtbFsl/KRE7p8SI=", "9XIGNQRkYuVFUqcUOklYlmfx+NTSob58DCl9npyrfYsOOyRIegEQgWnixTPvmCDQ", "9XIGNQRkYuVFUqcUOklYlg59FPmWWhwxfY4ynytLjZ4=", "y8Kx98A6zYTu3nr1L9lE4GpZfwt2DPB5jxAgOT9Yub4e+bHp6OLB6EQm+yEMeKZJ", "RNzeXXb7Za3QOnaC3lSNQXkwHhRX8iTNnuj6kvre2sM=", "wl3C1ZzMRUSTiPV+0R8s4sYIYWwgyISYO+Td+eBXaR8=", "wl3C1ZzMRUSTiPV+0R8s4p75xObwQXgdsmwD8xZrB3g=", "Wh9GiDBBj0J8tSnv/kDIsJsWpYesI1VB+XBqUJybTnU=", "/MHEeP0kURfFJCGMZ+lPiOMn+IZE/GXG5rSSw4X+Tj8=", "6BKMJ2atC9BXjMLCix612tgA/ZL+XyUrDa2uKYJDgv8=", "gu9aCNNKPGDBpl4rTjTlLZuWncguZP5GsWi52SULk14=", "pqounvH0p6Asu1lFgEqJPztb8UpM7B6z/f31sc/su0A=", "x+012IqvuLTgDXJLZp7UEVDyFyLwfid2ZJbxvRE1T/8=", "oImTYyinIKn9/D0CKW0bK9m1Stf3QAL3tclQl0g7EeM=", "MqwPYE22obdymaRgRym7x00CIfwCxOIL8JCJsK/DB3o=", "lZI9qZBI1iOer3gKd41ElM8KZ8FJKa53Ls4qOFuf7bs=", "H/hEWBtysQA7gHesbzRSeeaORLfOQ9PMhOsB9hz8umk=", "eBFDyuaVEX3QQeQonDdgQ283ACHwWSe7WM6NmG0sAGs=", "/MHEeP0kURfFJCGMZ+lPiAZL2XuoitE3R7FlRWs2ivQMSkv9wpNwCYEFo5HQpJA2", "lZI9qZBI1iOer3gKd41ElM8KZ8FJKa53Ls4qOFuf7bs=", "H/hEWBtysQA7gHesbzRSeeaORLfOQ9PMhOsB9hz8umk=", "eBFDyuaVEX3QQeQonDdgQ+xUZh/O9j/7ZDek/zEYsu0=", "/MHEeP0kURfFJCGMZ+lPiIkkqtmr9SakJTWK/bImC3c=", "OjaFJeXq0RyDyrDvSGp4zjNKQzfn5nMPeD84Xi9p/KQ=", "YERWnnYa92oDru27+bz2yHfvZk5vAxP9ddJH0vQH6/U=", "XVMQA2NH/iVPiQPCle92oUgtSMnrsZy1R5PkcC5PFcU=", "sRZKHFmR5ybhQ60ZROT2V9UqtwwapvFYZ3H5hIeKKno=", "FASbP04SAvFMsZ6nnlPguz9dPRQs3jnsJt/AasrcQgo=", "Fq98dA/qnsTU+JJqhUHW38dsTk7hHopDPJpvGBMYkBA=", "vUfIDFSK+COSdL9TBwsQ/YmMSbLviA2sOLJ7gq5iR5Ka3JcC1wm6PqRsMZzeXyrG", "SM9uLyYu/fNx82kU8pNWYYhWrVtcgdinRXpzoETbXIw=", "aTvVT9p4cOsxHTd98KHfYRueOacNWtYrijgGUi521Is=", "H/hEWBtysQA7gHesbzRSeeaORLfOQ9PMhOsB9hz8umk=", "y/C8cCAlWkQMbU3n0j2QTtPILfzKQjXeHleFjvd0/fc=", "/MHEeP0kURfFJCGMZ+lPiAZL2XuoitE3R7FlRWs2ivQMSkv9wpNwCYEFo5HQpJA2", "H/hEWBtysQA7gHesbzRSeeaORLfOQ9PMhOsB9hz8umk=", "lZI9qZBI1iOer3gKd41ElM8KZ8FJKa53Ls4qOFuf7bs=", "/MHEeP0kURfFJCGMZ+lPiOMn+IZE/GXG5rSSw4X+Tj8=", "y/C8cCAlWkQMbU3n0j2QTtPILfzKQjXeHleFjvd0/fc="};
            String[] payloads2 = {"WEmU8STpios2MRI5BTUcmw==", "aTcKorEdzNmqB4OJPG8frvJ2e9Ro/vhVz5K2p2lMe9c=", "v9oPUvf9Ibzq2A7m4tUXoLYq9UXWArPFg+5Q+aWZh31UFa8MFUwKL9nnFnjWZ2psADkoSAPC8dK2WwNMdKW1+OtSGS+aMadsroHxM7saGHY=", "unKLLjKneLygc5FojlmYEHsnNSTzH0/BWRJhZFU5TcyNWxPmc8Z5ZPe/pF0BncvXu6ZZx6cVSUx6kIVZwqakgA==", "UKgQv9uQpvnJslNYfXqeSWMiqNZuB56zzsx6xJ2bz2A=", "7uxs1YSjE0L+VNmLCCJHN0FANrZXe5P2BsHqxaV3xmA=", "d6BcHe8sTXik43mKGUockXH9fu+RGaBfmTT8qX7FaZE=", "n3Y+2ysYfFmZqaa0rqqUiMUVJfvgmyMuObyt2BLtvoo=", "kbJ7wCjEuzPDoumnsyaoHBo8qeCbb2VbmD5Zp3SH/jc=", "NCrV1UcZa4upE//qq46vYUPfzccnFOTLn+dV1Y5xA2U=", "wpwvg8hfcvkuJqARpULIVJ+SYcRAaPxyW/vcG9tbW0M=", "OibTJYXQhqxvVyFisj+vxXlCiXC7MUxZwe8kzOyxT4U=", "EAPNYoE6wW24F5i1voz8jh+j+01W1qZCoiM9QER1pDo=", "83MSIum4ZxOVDLv4RjTXesLxFTRrBrxxdsTp9hrMTW4bGjbQhsFhUY/OMhQ2mllD", "ddlDfoCY/18NqkUxI/0shtrHu4JUZgS8qplgRM/dBeU=", "OibTJYXQhqxvVyFisj+vxXlCiXC7MUxZwe8kzOyxT4U=", "xjg3CQV8276OnbShzACueWXJX2VL8icYMo90UbVJSfg=", "83MSIum4ZxOVDLv4RjTXemJyYUwb2BUS9/HvIjXniUE=", "xjg3CQV8276OnbShzACueRaGXqjkFc+HTlyjfNyyfeY=", "hyKs4xX9inWJsbxNB3B/ml0UsOD1EmRrBS87LJRcY5A=", "ddlDfoCY/18NqkUxI/0shtrHu4JUZgS8qplgRM/dBeU=", "Onc/ueSFNlHBPzq9BwQRxME2j/A+JHgDcrWrwRKwIWk=", "GjbJdg0s7AE6N/BcnCtdPGUFulWLKz7MgQx7I0SQLtw=", "DsKVMLzNTkbribZDm0cWT7Zs5/nXyM22PUvTt5/JUuk=", "W4YC++/NFwjw+7SfHUqycp0cC8f4Ehw09CJGQ+XLUfo=", "q01w3E450ec4RTN9YVELK2+wTfwLysttbP7Q3NxeySY=", "S3L05QFWV1WzfiNC1/aMTtFtgLtPNCr0040L7PavGM8=", "OibTJYXQhqxvVyFisj+vxXlCiXC7MUxZwe8kzOyxT4U=", "pCtj3PQvgeZ2WsX30TTjiU7WAlJ9EFyLw/64aEISLmQtE9mQS5sS85y5ep+Ca4Bu", "83MSIum4ZxOVDLv4RjTXesLxFTRrBrxxdsTp9hrMTW4bGjbQhsFhUY/OMhQ2mllD", "fDQ0vTQJmZtU8c1IJfeE01QGLQ0TQklTWIkhI1ZI8KA=", "ddlDfoCY/18NqkUxI/0shtrHu4JUZgS8qplgRM/dBeU=", "YPbw58eX1P14hEsj2eFAVFa32u2x4fETfXvwiW9q3oA=", "YPbw58eX1P14hEsj2eFAVFa32u2x4fETfXvwiW9q3oA=", "OibTJYXQhqxvVyFisj+vxXlCiXC7MUxZwe8kzOyxT4U=", "d6BcHe8sTXik43mKGUockXH9fu+RGaBfmTT8qX7FaZE=", "83MSIum4ZxOVDLv4RjTXej5SiKpzUMqdVjZsGVImhCk=", "unKLLjKneLygc5FojlmYECHQ5+WYRx2NSID0PyEnfrg="};
            System.out.println("Length payload: "+payloads2.length);
            for(int i =0;i<payloads.length;i++)
            {
                String dmgs = aes.decryptStrAndFromBase64(payloads2[i]);
                System.out.println(dmgs);
            }
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
       
    }
}