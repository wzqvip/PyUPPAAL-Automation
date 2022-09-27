from verifyta_path import VERIFYTA_PATH
from verifyta_path import ROOT_DIR
import os
import time
import pytest
from pyuppaal import Verifyta

# Verifyta().do_print()

# 命令行输入pytest -s可以查看print

def test_set_verifyta_path():
    with pytest.raises(ValueError) as excinfo:
        Verifyta().set_verifyta_path('invalid path')
    assert Verifyta().set_verifyta_path(VERIFYTA_PATH) == True
    
def test_verify():
    Verifyta().set_verifyta_path(VERIFYTA_PATH)
    model_paths = [os.path.join(ROOT_DIR, 'demo1.xml'), 
                   os.path.join(ROOT_DIR, 'demo2.xml'), 
                   os.path.join(ROOT_DIR, 'demo3.xml')]
    # 单线程循环
    t0 = time.time()
    verify_ress = Verifyta().verify(model_paths, verify_options = '-t 1 -o 0')
    for verify_res in verify_ress:
        assert 'satisfied' in verify_res
    t1 = time.time()
    # 多线程同步
    verify_ress = Verifyta().verify(model_paths, verify_options = ['-t 1 -o 0', '-t 2 -o 0', '-t 2 -o 1'], num_threads=3)
    for verify_res in verify_ress:
        assert 'satisfied' in verify_res
    t2 = time.time()
    # 单线程
    single_thread_time = round(t1-t0, 2)
    multi_thread_time = round(t2-t1, 2)
    assert single_thread_time > multi_thread_time
    print(f'3个复杂度相似单不完全相同任务, \n单线程: {single_thread_time}s, 单线程平均: {round(single_thread_time/3, 2)}s, 3线程: {multi_thread_time}s.')

def test_easy_verify():
    Verifyta().set_verifyta_path(VERIFYTA_PATH)
    model_paths = [os.path.join(ROOT_DIR, 'demo1.xml'), 
                   os.path.join(ROOT_DIR, 'demo2.xml'), 
                   os.path.join(ROOT_DIR, 'demo3.xml')]
    trace_paths = [os.path.join(ROOT_DIR, 't1.xtr'), 
                   os.path.join(ROOT_DIR, 't2-.xml'), 
                   os.path.join(ROOT_DIR, 't3-.xml')]
    Verifyta().easy_verify(model_paths, verify_options=['-t 1 -o 0', '-t 2 -o 0', '-t 2 -o 1'], num_threads=3)
    Verifyta().easy_verify(model_paths, trace_path=trace_paths, verify_options='-t 1 -o 0', num_threads=3)
    