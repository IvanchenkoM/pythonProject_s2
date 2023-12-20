import pytest
import yaml
import time

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(site, select_input_button, select_input_login, select_input_password, select_error):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys('test')
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys('test')
    btn = site.find_element('css', select_input_button)
    btn.click()
    err_label = site.find_element('xpath', select_error)
    assert err_label.text == '401'


def test_step_2(site, select_input_button, select_input_login, select_input_password, select_true_user):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    answer1 = site.find_element('xpath', select_true_user)
    assert answer1.text == f'Hello, {testdata["login"]}'


'''Условие: Добавить в наш тестовый проект шаг добавления поста после входа. Должна
выполняться проверка на наличие названия поста на странице сразу после его создания.

Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.

Что ещё можно почитать:
• Начинаем работать с Selenium в Python'''


def test_step_3(
        site,
        select_input_button,
        select_input_login,
        select_input_password,
        select_input_btn_create_post,
        select_input_post_title,
        select_input_post_description,
        select_input_post_content,
        select_input_btn_save_post,
        select_title_done_post,
):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    time.sleep(testdata['sleep_time_for_check'])
    btn_create_post = site.find_element('xpath', select_input_btn_create_post)
    btn_create_post.click()
    time.sleep(testdata['sleep_time_for_check'])
    input_post_title = site.find_element('xpath', select_input_post_title)
    input_post_title.send_keys(testdata['title_post'])
    input_post_description = site.find_element('xpath', select_input_post_description)
    input_post_description.send_keys(testdata['description_post'])
    input_post_content = site.find_element('xpath', select_input_post_content)
    input_post_content.send_keys(testdata['content_post'])
    time.sleep(testdata['sleep_time_for_check'])
    btn_save_post = site.find_element('xpath', select_input_btn_save_post)
    btn_save_post.click()
    time.sleep(testdata['sleep_time_for_check'])
    title_done_post = site.find_element("xpath", select_title_done_post)
    assert title_done_post.text == testdata['title_post']
