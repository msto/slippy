
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


rule rule_with_run_block:
    input:
        foo="foo.txt"
    output:
        bar="bar.txt"
    log:
        "logs/good_rule.log"
    run:
        print("hello world")


rule rule_with_script_block:
    input:
        foo="foo.txt"
    output:
        bar="bar.txt"
    log:
        "logs/good_rule.log"
    script:
        "scripts/script.py"


rule rule_with_no_log:
    input:
        foo="foo.txt"
    output:
        bar="bar.txt"
    shell:
        """
        (
        cat {input.foo} > {output.bar};
        ) &> {log}
        """

rule rule_with_no_log_redirection:
    input:
        foo="foo.txt"
    output:
        bar="bar.txt"
    log:
        "logs/good_rule.log"
    shell:
        """
        cat {input.foo} > {output.bar};
        """