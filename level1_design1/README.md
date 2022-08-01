# Multiplexer Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com/) provided for the hackathon.

![mux_window](https://user-images.githubusercontent.com/89663688/182241670-f0a163b4-dfa7-46c7-ad6d-ea4bac5054d6.PNG)

### Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. <br/>
The test drives inputs to the Design Under Test (Multiplexer module here) which takes in 31 inputs of 2 bit each, and a 5 bit select line, and has one output line that gives any of the input values depending on the select line. <br/><br/>

The Values are assigned to the inputs in the following way: <br/>
```
inp=[3,2,1,3]
for i in range(31):
exec(f'dut.inp{i}.value={inp[i%4]}')
```
And The select line is assigned by:
```
 dut.sel.value=12 #case-1
 dut.sel.value=13 #case-2
 dut.sel.value=30 #case-3
 ```

