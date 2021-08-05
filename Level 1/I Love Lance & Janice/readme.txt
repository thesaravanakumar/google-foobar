## I Love Lance & Janice

Time to solve: 48 hours.

### Description

You’ve caught two of your fellow minions passing coded notes back and forth – while they’re on duty, no less! Worse, you’re pretty sure it’s not job-related – they’re both huge fans of the space soap opera “Lance & Janice”. You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting her time passing non-job-related notes, it’ll put you that much closer to a promotion.

Fortunately for you, the minions aren’t exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched. That is, ‘a’ becomes ‘z’, ‘b’ becomes ‘y’, ‘c’ becomes ‘x’, etc. For instance, the word “vmxibkgrlm”, when decoded, would become “encryption”.

Write a function called answer(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about “Lance & Janice” instead of doing their jobs.

### Languages

To provide a Python solution, edit solution.py

To provide a Java solution, edit Solution.java

### Test cases

#### Test Case 1

Inputs:
```
(string) s = “wrw blf hvv ozhg mrtsg’h vkrhlwv?”
```
Output:
```
(string) “did you see last night’s episode?”
```

#### Test Case 2

Inputs:
```
(string) s = “Yvzs! I xzm’g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!”
```
Output:
```
(string) “Yeah! I can’t believe Lance lost his job at the colony!!”
```

### Constraints

#### Java

Your code will be compiled using standard Java 7. It must implement the answer() method in the solution stub.

Execution time is limited. Some classes are restricted (e.g. java.lang.ClassLoader). You will see a notice if you use a restricted class when you verify your solution.

Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.

#### Python

Your code will run inside a Python 2.7.6 sandbox.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.
