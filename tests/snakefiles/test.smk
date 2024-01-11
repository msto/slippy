
rule all:
    input:
        "test.txt"


rule good_rule:
    """test docstring"""
    input:
        foo="foo.txt"
    output:
        bar="bar.txt"
    log:
        "logs/good_rule.log"
    shell:
        """
        (
        cat {input.foo} > {output.bar};
        ) &> {log}
        """

rule rule_with_no_docstring:
    input:
        foo="foo.txt"
    output:
        bar="bar.txt"
    log:
        "logs/good_rule.log"
    shell:
        """
        (
        cat {input.foo} > {output.bar};
        ) &> {log}
        """
