from typing import Protocol
class Report(Protocol):
    def generate(self)->str:
        pass

class PdfReport(Report):
    def generate(self):
        return "PDF rapport"

class HtmlReport(Report):
    def generate(self):
        return "HTML rapport"

class ReportFactory:
    @staticmethod
    def create(report_type: str) -> Report:
        if report_type == "pdf":
            return PdfReport()
        elif report_type == "html":
            return HtmlReport()
        else:
            raise ValueError("Onbekend rapporttype")


report = ReportFactory.create("pdf")
print(report.generate())


class Creator(Protocol):

    def factory_method(self) -> Report:
        pass

    def do_something(self):
        report_gen = self.factory_method()
        return report_gen.generate()

class PdfCreator(Creator):
    def factory_method(self):
        return PdfReport()

pc_creator = PdfCreator()
print(pc_creator.do_something())



