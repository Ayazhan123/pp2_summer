class Solution:
    def interpret(self, command: str) -> str:
        x=command.replace("()","o")
        return (x.replace("(al)","al"))