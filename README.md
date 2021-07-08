# frida-expose-hawkcredentials
Hook HawkCredentials > initWithHawkId:withKey:withAlgorithm: calls and log the HawkId and key used by various iOS apps.

Device used: iPhone X (GSM), iOS 14.4 with checkra1n jailbreak

## Example
![image](https://user-images.githubusercontent.com/9308774/124964001-7f8ba200-dfee-11eb-9d73-010304a11b65.png)


## References
### Jailbreak Related
https://docs.google.com/spreadsheets/d/11DABHIIqwYQKj1L83AK9ywk_hYMjEkcaxpIg6phbTf0/edit#gid=1014970938

https://www.theiphonewiki.com/wiki/Jailbreak/14.x#cite_note-semi-tethered-3

https://github.com/rcg4u/iphonessh


### Hawk Related
https://blog.mozilla.org/services/2015/02/05/whats-hawk-and-how-to-use-it/

https://mohawk.readthedocs.io/en/latest/usage.html

https://github.com/ibadus/hawk-mesh-go

https://github.com/tent/hawk-objc

https://github.com/VastidDev/Mesh-Keys

### Frida Related
https://build.frida.re

https://medium.com/infosec-adventures/introduction-to-frida-5a3f51595ca1

https://11x256.github.io/Frida-hooking-android-part-2/

https://github.com/trelis24/frida-ios/blob/master/find_classes.js

https://github.com/trelis24/frida-ios/blob/master/hooking.js

https://github.com/trelis24/frida-ios/

https://trelis24.github.io/

https://joshspicer.com/android-frida-1

https://www.trustedsec.com/blog/mobile-hacking-using-frida-to-monitor-encryption/

https://11x256.github.io/Frida-hooking-android-part-5/

https://brandonevans.ca/post/text/how-i-reverse-engineer-ios-apps/

https://fadeevab.com/quick-start-with-frida-to-reverse-engineer-any-ios-application/

https://www.frida.re/docs/installation/

https://frida.re/docs/examples/ios/

https://frida.re/docs/ios/

https://frida.re/docs/quickstart/

https://frida.re/docs/frida-trace/

https://la0s.github.io/2018/12/07/iOS_Crypto/

https://www.virtuesecurity.com/kb/ios-frida-objection-pentesting-cheat-sheet/

https://github.com/AloneMonkey/dumpdecrypted

https://github.com/noobpk/frida-ios-hook

https://github.com/AloneMonkey/frida-ios-dump

https://github.com/integrity-sa/frida-ipa-dump

https://github.com/iddoeldor/frida-snippets

https://github.com/Nightbringer21/fridump

https://duffy.app/frida-extract/

https://fadeevab.com/decrypt-ios-applications-3-methods/

https://reverseengineering.stackexchange.com/questions/21881/how-does-ipa-decryption-works

https://ivrodriguez.com/decrypting-ios-applications-ios-12-edition/

https://www.programmersought.com/article/1175724927/

https://www.programmersought.com/article/18377049506/

https://book.hacktricks.xyz/mobile-apps-pentesting/android-app-pentesting/frida-tutorial

https://stackoverflow.com/questions/52422675/how-to-extract-contents-from-a-ipa-file-2018

https://thelinuxos.com/how-to-setup-and-install-frida-and-objection-on-macos/

http://pentestcorner.com/introduction-to-fridump/

https://mobile-security.gitbook.io/mobile-security-testing-guide/ios-testing-guide/0x06j-testing-resiliency-against-reverse-engineering

http://blog.itselectlab.com/?p=10498

https://awesomeopensource.com/project/dweinstein/awesome-frida

https://www.jianshu.com/p/d7976fff77e8

https://ub3rsick.github.io/2019/10/22/ios-ipa-dump-decrypted/
