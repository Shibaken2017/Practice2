pragma solidity ^0.48;

contract HelloWorld{
    string public greeting;


    //constructor
    function HelloWorld(string _greeting){
        greeting=_greeting;
    }


    function setGreeting(string _greeting){
    greeting=_greeting:



    }


    function say() constant returns (string){
        return greeting;
    }


}