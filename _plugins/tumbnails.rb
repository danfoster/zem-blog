require 'nokogiri' # gem install nokogiri

module Jekyll
  module ImageFilter
    def extract_img(input)
      doc = Nokogiri::HTML( input )
      output = ""
      img_srcs = doc.css('img')
      img_srcs[0..5].each do |img|
          img['class'] = "sidebar_thumbnail"
          output = output + "#{img.to_s}"
      end
      return output
    end
  end
end

Liquid::Template.register_filter(Jekyll::ImageFilter)
