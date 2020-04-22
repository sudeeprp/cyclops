import os
from behave import *

BASELINE_REPORTNAME = 'baseline'
UPDATED_REPORTNAME = 'updated'

def run_lizard(sourcefile, reportname):
    print(f'lizard {sourcefile} -o {reportname}.csv')
    return os.system(f'lizard {sourcefile} -o {reportname}.csv')

def run_cyclops(threshold):
    return os.system(f'python comparecyclo.py {threshold} {UPDATED_REPORTNAME}.csv {BASELINE_REPORTNAME}.csv')


LANG_BASELINE_MAP = {
    'java': ('baseline-java', '.java'),
    'python': ('baseline-python', '.py'),
    'cpp': ('baseline-cpp', '.cpp')
}
SOURCE_LOCATION = 'features'

@given('a baseline {lang} source')
def report_on_baseline(context, lang):
    baseline_source = LANG_BASELINE_MAP[lang]
    baseline_srcpath = os.path.join(SOURCE_LOCATION,
                                    baseline_source[0] + baseline_source[1])
    run_lizard(baseline_srcpath, BASELINE_REPORTNAME)
    context.lang = lang

@given('a complexity threshold of {threshold}')
def set_threshold(context, threshold):
    context.threshold = threshold

@when('run on an update {update_name}')
def report_on_update(context, update_name):
    baseline_source = LANG_BASELINE_MAP[context.lang]
    updated_source = baseline_source[0] + '-' +\
                     update_name.replace(' ', '-') + baseline_source[1]
    updated_srcpath = os.path.join(SOURCE_LOCATION, updated_source)
    run_lizard(updated_srcpath, UPDATED_REPORTNAME)

@then('the gate fails')
def assert_failure(context):
    assert run_cyclops(context.threshold) == 1

@then('the gate passes')
def assert_passing(context):
    assert run_cyclops(context.threshold) == 0
