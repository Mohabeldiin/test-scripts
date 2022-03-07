"""a Module to interact with Google PageSpeed Insights API"""
import urllib.request
import json


def ApiSpeed(website: str):
    """Test Website Performance

        Args:
            website: URL of WebSite to Test

        Returns:
            Print Website Performance.

        Example:
            ApiSpeed(URL)
    """
    url: str = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&strategy=desktop&key=AIzaSyCcDNbRIvDPnuOM1TdCwoyzmP6NiGOkcLU".format(website)
    """API Request
        parameter:
            url: WebSite Link to Test
            strategy: testing environment either {mobile, desktop}
            key: API Key
    """

    response = urllib.request.urlopen(url)
    """Requesting Performance Evaluation"""

    data = json.loads(response.read())
    """Fetch JSON Response"""

    fcp = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
    """First Contentful Paint of loadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    fid = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
    """First Input Delay of loadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    lcp = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
    """Largest Contentful Paint of loadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    cls = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
    """Cumulative Layout Shift Score of loadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    overall = data["loadingExperience"]["overall_category"]
    """Overall Performance of loadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """

    print("\n")
    print("loadingExperience:")
    print("First Contentful Paint: {}".format(fcp))
    print("First Input Delay: {}".format(fid))
    print("Largest Contentful Paint: {}".format(lcp))
    print("Cumulative Layout Shift Score: {}".format(cls))
    print("Overall Performance: {}".format(overall))
    print("")

    fcp = data["originLoadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
    """First Contentful Paint of OriginLoadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    fid = data["originLoadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
    """First Input Delay of OriginLoadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    lcp = data["originLoadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
    """Largest Contentful Paint of OriginLoadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    cls = data["originLoadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
    """Cumulative Layout Shift Score of OriginLoadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """
    overall = data["originLoadingExperience"]["overall_category"]
    """Overall Performance of OriginLoadingExperience
        :returns: Four type of performances: “Slow“, “Average”, “None” and “Fast“.
    """

    print("\n")
    print("originLoadingExperience:")
    print("First Contentful Paint: {}".format(fcp))
    print("First Input Delay: {}".format(fid))
    print("Largest Contentful Paint: {}".format(lcp))
    print("Cumulative Layout Shift Score: {}".format(cls))
    print("Overall Performance: {}".format(overall))
    print("")

    fcp = data["lighthouseResult"]["audits"]["first-contentful-paint"]["displayValue"]
    """First Contentful Paint of lighthouseResult
        :returns: in Seconds.
    """
    tto = data["lighthouseResult"]["audits"]["interactive"]["displayValue"]
    """Time to Interactive of lighthouseResult
        :returns: in Seconds.
    """
    lcp = data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"]
    """Largest Contentful Paint of lighthouseResult
        :returns: in Seconds.
    """
    cls = data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"]
    """Cumulative Layout Shift Score of lighthouseResult
        :returns: in Seconds.
    """
    tbt = data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"]
    """Total Blocking Time of lighthouseResult
        :returns: in Seconds.
    """
    si = data["lighthouseResult"]["audits"]["speed-index"]["displayValue"]
    """Speed Index of lighthouseResult
        :returns: in Seconds.
    """

    print("\n")
    print("lighthouseResult:")
    print("First Contentful Paint: {}".format(fcp))
    print("Time to Interactive: {}".format(tto))
    print("Largest Contentful Paint: {}".format(lcp))
    print("Cumulative Layout Shift Score: {}".format(cls))
    print("Total Blocking Time: {}".format(tbt))
    print("Speed Index: {}".format(si))
    print("")

    overall_performance = data["lighthouseResult"]["categories"]["performance"]["score"] * 100
    """Overall Performance of lighthouseResult
        :returns: performances: in Percentage.
    """
    print("Overall Performance: {}".format(overall_performance))
    print("")


if __name__ == "__main__":
    ApiSpeed("https://facebook.com")
