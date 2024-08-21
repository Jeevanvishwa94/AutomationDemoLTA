from Pageobject.book_a_group_page import BookGroupLesson
from testcase.base_test import BaseTest
from utilities.test_data import TestData


class TestBookAGroup(BaseTest):

    def test_book_a_gropu_lesson(self):
        book_group_lesson = BookGroupLesson(self.driver)
        book_group_lesson.lta_username(TestData.Username)
        book_group_lesson.lta_password(TestData.Password)
        book_group_lesson.click_lta_login()
        book_group_lesson.Accept_all_cookies()
        element = book_group_lesson.find_element(*book_group_lesson.locate.play)
        book_group_lesson.hover_over_element(element)
        book_group_lesson.play_module()
        element = book_group_lesson.find_element(*book_group_lesson.locate.remove_location)
        book_group_lesson.hover_over_element(element)
        book_group_lesson.group_lesson_checkbox("Wimbledon, London, UK")
        book_group_lesson.group_lesson_dropdown()
        book_group_lesson.find_a_court() 
        book_group_lesson.Recurring()
        book_group_lesson.Recurring_dropdown_box()
        # book_group_lesson.session_dropdown()
        # book_group_lesson.group_session_book_class()
        
        