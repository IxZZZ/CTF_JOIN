def generateKeyAndIV():
        iv = "0123456789abcdef"
        ivBytes = [ord(i) for i in "0123456789abcdef"]
        a = []
        a[0] = ((ivBytes[13] + ivBytes[12]) - (ivBytes[1] + ivBytes[2]))
        a[2] = ((((ivBytes[11] * 2) - (ivBytes[0] * 3)) - ivBytes[2]) + 1)
        a[15] = ((a[2] * 16) - (51 / a[2]))
        a[9] = (
            (((((ivBytes[3] + ivBytes[4]) + ivBytes[5]) + 1) - ivBytes[0]) - ivBytes[1]) / 3)
        a[1] = ((((a[0] * 2) - a[15]) - (ivBytes[2] * 2)) + a[9])
        a[3] = (a[0] - 36)
        a[4] = (a[0] / a[9])
        a[5] = (a[6] * (a[9] / 2))
        a[6] = ((a[9] / 2) - a[2])
        a[5] = (a[6] * (a[9] / 2))
        a[7] = a[4]
        a[8] = (
            (((a[7] * a[6]) + ((a[2] * a[4]) * a[7])) - a[0]) - (a[0] / 10))
        a[13] = (((ivBytes[2] * 2) - (a[0] / 2)) - a[2])
        a[10] = ((ivBytes[13] - ivBytes[2]) - a[13])
        a[11] = ((a[9] * 4) + a[2])
        a[12] = (a[9] + a[2])
        a[14] = a[8]
        s = ""
        for i in range(16):
            a[i] = (a[i] ^ ivBytes[i])
            s = s + chr(a[i])
        key = s


def encrypt(ivStr, keyStr, bytes):
        keyBytes = keyStr.getBytes("UTF-8")
        AlgorithmParameterSpec ivSpec = new IvParameterSpec(ivStr.getBytes("UTF-8"))
        SecretKeySpec newKey = new SecretKeySpec(keyBytes, "AES")
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding")
        cipher.init(1, newKey, ivSpec)
        return cipher.doFinal(bytes)


def encryptStrAndToBase64(String pt):
        return new String(Base64.encode(encrypt(this.iv, this.key, pt.getBytes("UTF-8")), 2), "UTF-8")


def decrypt(String ivStr, String keyStr, bytes):
        keyBytes = keyStr.getBytes("UTF-8")
        AlgorithmParameterSpec ivSpec = new IvParameterSpec(ivStr.getBytes("UTF-8"))
        SecretKeySpec newKey = new SecretKeySpec(keyBytes, "AES")
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding")
        cipher.init(2, newKey, ivSpec)
        return cipher.doFinal(bytes)


def decryptStrAndFromBase64(String ct):
        return new String(decrypt(this.iv, this.key, Base64.decode(ct.getBytes("UTF-8"), 2)), "UTF-8")


def getSHA256(String pltext):
        MessageDigest sha = MessageDigest.getInstance("SHA-256")
        sha.update(pltext.getBytes())
        return sha.digest()


def bytesToHex(hash) {
        StringBuilder hexString = new StringBuilder(hash.length * 2)
        for (byte b: hash) {
            String hex = Integer.toHexString(b & 255)
            if (hex.length() == 1) {
                hexString.append('0')

            hexString.append(hex)

        return hexString.toString()
